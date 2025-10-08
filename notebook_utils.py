import openai

openai.api_key = "YOUR_API_KEY_HERE"

def summarize(note: str) -> str:
    """
    Summarizes a single note using OpenAI's LLM.
    """
    prompt = f"Summarize this note concisely:\n\n{note}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )
    summary = response.choices[0].message['content'].strip()
    return summary
