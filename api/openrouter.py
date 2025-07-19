import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def call_openrouter(prompt):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return "❌ OpenRouter API key not found in .env"

    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",  
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
