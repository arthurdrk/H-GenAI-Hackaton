import gradio as gr
import boto3
import json
import time
from ChatbotLib import chat_with_model, convert_chat_messages_to_converse_api


# Client AWS Bedrock
bedrock = boto3.client("bedrock-runtime", region_name="us-west-2")

def generate_content(prompt):
    chat_en_cours = chat_with_model(new_text=prompt)
    chat_messages = convert_chat_messages_to_converse_api(chat_en_cours)
    reponse = chat_messages[-1]["content"][0]["text"]
    
    return reponse
    
def process_request_with_loading(prompt):
    """Affiche un message de chargement avant la génération."""
    yield "<b>⏳ Génération en cours... Patientez...</b>"
    time.sleep(2)  

    result = generate_content(prompt)   

    yield f"<b>📝 Résultat :</b><br>{result}"

# Création de l'interface Gradio
with gr.Blocks(theme=gr.themes.Soft()) as iface:
    gr.Markdown("# 📝 Générateur de Texte avec AWS Bedrock")
    gr.Markdown("### Entrez votre prompt ci-dessous pour générer du texte.")

    with gr.Row():
        prompt_input = gr.Textbox(label="🔹 Entrez votre prompt", placeholder="Décrivez le texte souhaité...", lines=3)

    with gr.Row():
        generate_btn = gr.Button("🚀 Générer le texte")
    
    output_text = gr.HTML(visible=True)  

    generate_btn.click(
        fn=process_request_with_loading,
        inputs=prompt_input,
        outputs=output_text
    )

iface.launch(share=True)
