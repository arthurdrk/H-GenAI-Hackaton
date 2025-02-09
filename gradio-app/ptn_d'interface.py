import gradio as gr
import boto3
import json
import time

# Client AWS Bedrock
bedrock = boto3.client("bedrock-runtime", region_name="us-west-2")

def generate_content(prompt):
    try:
        # Appel au modèle AWS Bedrock pour générer le contenu
        response = bedrock.invoke_model(
            modelId="mistral.mistral-large-2407-v1:0",  # Remplacer par notre modèle spécifique
            body=json.dumps({"inputText": prompt})
        )

        content = response["body"].read().decode("utf-8")  # Récupérer le contenu généré
        return content  # Retourner le contenu généré (HTML, PDF, etc.)
    except Exception as e:
        return f"Erreur lors de la génération du contenu: {str(e)}"

def process_request_with_loading(prompt):
    # Afficher un message de chargement avant la génération
    yield "⏳ Génération en cours... Patientez, cela prend un instant.", None  # Retourne deux valeurs
    time.sleep(2)  # Simule un temps de traitement

    # Processus pour générer le contenu
    result = generate_content(prompt)
    
    # Créer un fichier temporaire avec le contenu généré
    with open("generated_content.txt", "w", encoding="utf-8") as file:
        file.write(result)
    
    yield result, "generated_content.txt"  # Retourne le contenu généré et le fichier

# Création de l'interface Gradio avec un design moderne
with gr.Blocks(theme=gr.themes.Soft()) as iface:
    gr.Markdown("# 📝 Générateur de Document avec AWS Bedrock")
    gr.Markdown("### Entrez votre prompt ci-dessous pour générer un document")

    with gr.Row():
        prompt_input = gr.Textbox(label="🔹 Entrez votre prompt", placeholder="Décrivez le document souhaité...", lines=3)

    with gr.Row():
        generate_btn = gr.Button("🚀 Générer le document")
    
    output_text = gr.HTML(visible=True)  # Sortie sous forme de HTML
    output_file = gr.File(visible=True)  # Fichier pour télécharger le document généré

    # Ajout de la fonction avec progression
    generate_btn.click(
        fn=process_request_with_loading,
        inputs=prompt_input,
        outputs=[output_text, output_file]
    )

# Lancer l'interface
iface.launch(share=True)