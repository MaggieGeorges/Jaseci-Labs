import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env
load_dotenv()

# Get API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_note_with_llm(note: str) -> str:
    prompt = f"Summarize this note concisely:\n\n{note}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )
    return response.choices[0].message['content'].strip()
