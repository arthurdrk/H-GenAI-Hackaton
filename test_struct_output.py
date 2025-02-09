import boto3
import json

session = boto3.Session()
bedrock = session.client(service_name="bedrock-runtime")

content = """Dear Acme Investments,

I am writing to compliment one of your customer service representatives, Shirley Scarry. I recently had the pleasure of speaking with Shirley regarding my account deposit. Shirley was extremely helpful and knowledgeable, and went above and beyond to ensure that all of my questions were answered. Shirley also had Robert Herbford join the call, who wasn't quite as helpful. My wife, Clara Bradford, didn't like him at all.
Shirley's professionalism and expertise were greatly appreciated, and I would be happy to recommend Acme Investments to others based on my experience.
Sincerely,

Carson Bradford
"""

# Modèle JSON attendu
schema = {
    "summary": "string",
    "escalate_complaint": "boolean",
    "level_of_concern": "integer",
    "overall_sentiment": "string",
    "supporting_business_unit": "string",
    "customer_names": ["string"],
    "sentiment_towards_employees": [
        {
            "employee_name": "string",
            "sentiment": "string"
        }
    ]
}

# 🔥 Nouveau prompt ultra-directif
prompt = f"""
You are a data extraction AI. Convert the following email into a structured JSON format.

### JSON OUTPUT FORMAT:
{json.dumps(schema, indent=4)}

### EMAIL CONTENT:
{content}

### INSTRUCTIONS:
- **ONLY** output valid JSON.
- The response **MUST** be enclosed between `<json>` and `</json>`.
- No explanations, no additional text.

### RESPONSE:
<json>
"""

# Appel à Bedrock
response = bedrock.invoke_model(
    modelId="mistral.mistral-large-2407-v1:0",
    body=json.dumps({
        "prompt": prompt,
        "max_tokens": 500,
        "temperature": 0
    })
)

# Extraction de la réponse brute
response_body = json.loads(response["body"].read())
print(response_body)