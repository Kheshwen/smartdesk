# tasks.py
from config import OPENAI_API_KEY
import openai

# New OpenAI Client (v1.x)
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def prioritize_tasks(tasks):
    prompt = "Prioritize the following tasks based on urgency and importance:\n\n" + "\n".join(f"- {task}" for task in tasks)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a productivity assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract text from response
    prioritized_text = response.choices[0].message.content
    return prioritized_text.strip().split("\n")
