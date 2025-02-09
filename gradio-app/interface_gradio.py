import boto3
import json

# Configuration AWS Bedrock
bedrock = boto3.client("bedrock-runtime", region_name="us-west-2")

def generate_document(prompt):
    response = bedrock.invoke_model(
        modelId="bedrock-foundation-model-id",  # Remplacer par le bon modèle
        body=json.dumps({"inputText": prompt})
    )
    
    response_body = json.loads(response["body"].read().decode("utf-8"))
    return response_body.get("outputText", "Erreur dans la génération du document")

import gradio as gr

# Interface Gradio
iface = gr.Interface(
    fn=generate_document,
    inputs=gr.Textbox(label="Quelles informations recherchez-vous ?"),
    outputs=gr.Textbox(label="Document généré"),
    title="Evaluation des actions mises en place par les collectivités face aux risques climatiques"
)

# Lancer l'interface
iface.launch()
