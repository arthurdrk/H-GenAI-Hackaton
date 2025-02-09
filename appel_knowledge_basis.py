import boto3

# Configurer le client Bedrock
client = boto3.client('bedrock-agent-runtime', region_name='us-west-2')
# # Identifiant du Knowledge Base
# knowledge_base_id = "XBWFQCFXVI"
# model_id = "mistral.mistral-large-2407-v1:0"
# model_arn = "arn:aws:bedrock:model/anthropic.claude-v2"
# session_id = str(uuid.uuid4())
# Identifiants
knowledge_base_id = "XBWFQCFXVI"  # Remplace par ton ID de Knowledge Base
model_arn = "arn:aws:bedrock:us-west-2::foundation-model/mistral.mistral-large-2402-v1:0"  # Remplace par l'ARN correct du modèle
kms_key_arn = "arn:aws:kms:us-west-2:248189928368:key/f1e5827c-133a-4713-b2fa-11d689fe687c"  # Remplace par ton KMS Key ARN
modelId = "mistral.mistral-large-2402-v1:0"



def retrieve_info_from_rag(query):
    
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
                        "maxTokens": 8100,
                        "stopSequences": ["###"],
                        "temperature": 0.7,
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
    return response["output"]["text"] #["retrievalResults"][1]["content"]["text"])


# collectivite = 'Saint-Nazaire'

# prompt = f""" A l'aide de ta base de connaissance, analyse dans tous les documents les risques encourue par {collectivite}
# et les alentours. Si cette collectivité n'est pas présente dans ta base de connaissance, ne me donne pas d'info supplémentaire
# et préviens moi seulement de l'absence de cette collectivité. Si tu as bien accès à ces conaissances, fait moi une liste des 3 
# risques les plus importants par ordre décroissant. Ensuite, analyse pour chacun de ces risques, les mesures de prévention mise 
# en place par les collectivité pour les éviter. Si et seulement si les résultats de ces mesures sont décrites dans les documents,
# donne moi les résultats de ces mesures. Tu ne dois jamais inventer de donnée non présente dans les documents. Si tu n'a pas d'information
# sur un risque ou une mesure, répond seulement que tu ne sais pas a propos de ce risque"""

# retrieve_info_from_rag(prompt)

