from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def Generate_Roadmap(role):
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key= os.getenv("GENAI_API_KEY"),
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:cerebras",
        messages=[{"role": "user", "content": f"Give me RoadMap of {role}"}],
    )

    return response.choices[0].message.content

print(Generate_Roadmap("software engineer"))