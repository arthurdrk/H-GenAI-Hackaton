import boto3
import json
from gradio_app.ChatbotLib import *
import copy
from botocore.client import Config
import ast


# Configurer le client Bedrock
client = boto3.client('bedrock-agent-runtime', region_name='us-west-2')
# # Identifiant du Knowledge Base
# knowledge_base_id = "XBWFQCFXVI"
# model_id = "mistral.mistral-large-2407-v1:0"
# model_arn = "arn:aws:bedrock:model/anthropic.claude-v2"
# session_id = str(uuid.uuid4())
# Identifiants
region = "us-west-2"
bedrock_config = Config(connect_timeout=120, read_timeout=120, retries={'max_attempts': 0})
bedrock_agent_client = boto3.client("bedrock-agent-runtime",
                              region_name=region,
                              config=bedrock_config,
                                    )
knowledge_base_id = "XBWFQCFXVI"  # Remplace par ton ID de Knowledge Base
model_arn = "arn:aws:bedrock:us-west-2::foundation-model/mistral.mistral-large-2402-v1:0"  # Remplace par l'ARN correct du modèle
kms_key_arn = "arn:aws:kms:us-west-2:248189928368:key/f1e5827c-133a-4713-b2fa-11d689fe687c"  # Remplace par ton KMS Key ARN
modelId = "mistral.mistral-large-2402-v1:0"


#Bucket Setup
bucket_name = "dev-aws-bucket-jesaispas"
s3 = boto3.client("s3")


def retrieveAndGenerate(input, document_s3_uri, sourceType="S3", model_id = "anthropic.claude-3-sonnet-20240229-v1:0"):
    model_arn = f'arn:aws:bedrock:{region}::foundation-model/{model_id}'
    if sourceType=="S3":
        response = bedrock_agent_client.retrieve_and_generate(
            input={
                'text': input
            },
            retrieveAndGenerateConfiguration={
                'type': 'EXTERNAL_SOURCES',
                'externalSourcesConfiguration': {
                    'modelArn': model_arn,
                    "sources": [
                        {
                            "sourceType": sourceType,
                            "s3Location": {
                                "uri": document_s3_uri
                            }
                        }
                    ]
                }
            }
        )
        return response["output"]["text"]

def retrieve_and_generate_info_from_rag(query):
    
    # Appel à l'API de Bedrock
    response = client.retrieve_and_generate(
    input={"text": query},
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": knowledge_base_id,
            "modelArn": model_arn,
            "generationConfiguration": {
                "inferenceConfig": {
                    "textInferenceConfig": {
                        "maxTokens": 8192,
                        "stopSequences": ["###"],
                        "temperature": 0.3,
                        "topP": 0.9
                    }
                },
                "promptTemplate": {
                    "textPromptTemplate": "Voici les informations pertinentes trouvées :\n\n$search_results$\n\nRéponds à la question suivante en utilisant ces résultats : {query}"
                }
            }
        }
    },
    sessionConfiguration={
        "kmsKeyArn": kms_key_arn
    },
)

    # Afficher les résultats
    return response["output"]["text"]

def create_new_json():
    schema = {
        "document": {
            "nom": "",
            "annee_edition": -1,
            "lien": "string"
        },
        "synthese": {
            "objectif": "",
            "contenu": []
        },
        "identification_risques": [
            {
            "type_de_risque": "",
            "description": "",
            "zones_concernees": [],
            "exemples_passes": []
            }
        ],
        "actions_adaptation": {
            "mesures_preventives": [],
            "mesure_compensatoire" : [],
        },
        "niveau_confiance": {
            "pertinence": {
            "note": -1,
            "commentaire": ""
            },
            "exhaustivite": {
            "note": -1,
            "commentaire": ""
            },
            "lisibilite": {
            "note": -1,
            "commentaire": ""
            }
        }
    }
    return copy.deepcopy(schema)

def list_all_s3_files(prefix="Document gestions des risques en France"):
    files = []
    continuation_token = None

    while True:
        list_params = {"Bucket": bucket_name, "Prefix": prefix}
        if continuation_token:
            list_params["ContinuationToken"] = continuation_token

        response = s3.list_objects_v2(**list_params)
        if "Contents" in response :

            files.extend(obj["Key"] for obj in response["Contents"])

        if not response.get("IsTruncated"):  # Plus de pages à récupérer
            break

        continuation_token = response.get("NextContinuationToken")
    titre_doc = []
    for file in files:
        n = len(file)
        if file[n-3::] == "pdf":
            titre_doc.append(file)
            
    return titre_doc

def doc_to_json(doc_name, commune = "Avignon", risque = "risque d'inondation"):
    prefix_file_name = "<replace with the file name in your bucket>" #include prefixes if any alongwith the file name.
    document_s3_uri = f's3://{bucket_name}/{doc_name}'
    
    prompt1 = """Tu es un spécialiste de l'analyse des risques, tu dois analyser ce document et me dire s'il concerne bien {commune} et 
    s'il traite des {risque}. Si c'est le cas répond seulement "oui" et sinon seulement "non". Ne donne pas d'autres informations, explication,
    répond seulement oui si le document traite de {commune} ou ses environs ET s'il traite aussi des {risque}. Dans tous les autres cas répond seulement non."""
    
    reponse1 = retrieveAndGenerate(input = prompt1, document_s3_uri = document_s3_uri)
    
    schema = {
        "document": {
            "nom": "string",
            "annee_edition": "int",
            "lien": "string",
            "organisme_responsable": "string",
        },
        "synthese": {
            "objectif": "string",
            "contenu": "list of string"
        },
        "identification_risques": [
            {
            "type_de_risque": "string",
            "description": "string",
            "zones_concernees": "list of string",
            "exemples_passes": "list of int"
            }
        ],
        "actions_adaptation": {
            "mesures_preventives": "list of string",
            "mesure_compensatoire" : "list of string",
        },
        "niveau_confiance": {
            "pertinence": {
            "note": "int",
            "commentaire": "string"
            },
            "exhaustivite": {
            "note": "int",
            "commentaire": "string"
            },
            "lisibilite": {
            "note": "int",
            "commentaire": "string"
            }
        }
    }

    prompt2 = f"""Tu es un spécialiste de l'analyse des risques naturels et technologiques. Analyse les données présentes dans le fichier {document_s3_uri} 
    et renvoie un fichier JSON compléter suivant le format suivant
    
    ### JSON OUTPUT FORMAT: {json.dumps(schema, indent=4)}
    
    ### INSTRUCTIONS:
    - **ONLY** output valid JSON.
    - The response **MUST** be enclosed between `<json>` and `</json>`.
    - No explanations, no additional text.
    - If you don't have the information you **MUST** replace it by "N/A" and DO NOT create data not present in the document
    
    ### REPONSE:
    <json>
    """
    
    if reponse1.lower() =="oui":
        json_data = ast.literal_eval(retrieveAndGenerate(input = prompt2, document_s3_uri = document_s3_uri))
        json_data["document"]["nom"] = doc_name.split("/")[-1]
        json_data["document"]["lien"] = document_s3_uri
        json_data["identification_risques"][0]["type_de_risque"] = risque
        return json_data
    else: 
        return None
        
    
def get_all_documents():
    documents = list_all_s3_files()
    all_doc_json = []
    for doc in documents:
        resultat = doc_to_json(doc)
        if resultat != None:
            all_doc_json.append(resultat)
    return all_doc_json