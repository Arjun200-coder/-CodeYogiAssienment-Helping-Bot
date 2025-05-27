import os
import requests

api_key = os.getenv("DEEPSEEK_API_KEY")

def generate_code(prompt):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    if response.status_code != 200:
        print("❌ ERROR:", response.text)
        return "⚠️ DeepSeek API error"

    return response.json()['choices'][0]['message']['content']
