import boto3
import pandas as pd
import json
import re

# Initialisation des clients AWS
s3_client = boto3.client("s3")
bedrock_client = boto3.client("bedrock-runtime", region_name="us-west-2")

BUCKET_NAME = "dev-aws-bucket-jesaispas"  # Mon bucket S3

def lister_fichiers_s3():
    """Récupère la liste des fichiers dans le bucket S3"""
    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
    return [f["Key"] for f in response.get("Contents", [])]

def lire_fichier_s3(nom_fichier):
    """Lit un fichier CSV ou JSON depuis S3"""
    obj = s3_client.get_object(Bucket=BUCKET_NAME, Key=nom_fichier)
    if nom_fichier.endswith(".csv"):
        return pd.read_csv(obj["Body"]).to_dict(orient="records")
    elif nom_fichier.endswith(".json"):
        return json.loads(obj["Body"].read().decode("utf-8"))
    return None

def extraire_risques(donnees):
    """Extraire les lignes liées aux risques dans les données"""
    risques = []
    for ligne in donnees:
        # Exemple : on suppose que les risques sont des lignes contenant 'risque' ou 'danger'
        if any(re.search(r"(risque|danger|problème)", str(valeur), re.I) for valeur in ligne.values()):
            risques.append(ligne)
    return risques

def appeler_bedrock(donnees, prompt_utilisateur):
    """Envoie un prompt enrichi à AWS Bedrock pour extraire les risques"""
    prompt = f"Voici des données récupérées sur les risques : {json.dumps(donnees, indent=2)}.\n" \
             f"L'utilisateur demande : {prompt_utilisateur}. Peux-tu lister les risques sous la forme 'Risque 1 : ...' ?"

    response = bedrock_client.invoke_model(
        modelId="anthropic.claude-v2",  # Adapter selon le modèle
        body=json.dumps({"prompt": prompt, "max_tokens": 500})
    )
    return json.loads(response["body"].read().decode("utf-8"))["completion"]

def lambda_handler(event, context):
    """Fonction principale Lambda qui analyse automatiquement les fichiers pour extraire les risques"""
    try:
        # 📌 Récupération du prompt utilisateur
        body = json.loads(event["body"])
        prompt_utilisateur = body.get("prompt", "Quels sont les risques dans ces données ?")

        # 📌 Lecture automatique de tous les fichiers S3
        fichiers = lister_fichiers_s3()
        donnees = []
        for fichier in fichiers:
            donnees.extend(lire_fichier_s3(fichier) or [])

        # 📌 Extraction des risques des données (Retrieval)
        risques = extraire_risques(donnees)

        # 📌 Envoi des données pertinentes à AWS Bedrock pour analyse (Augmented Generation)
        reponse_bedrock = appeler_bedrock(risques, prompt_utilisateur)

        return {
            "statusCode": 200,
            "body": json.dumps({"reponse_bedrock": reponse_bedrock})
        }

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
