import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def prioritize_tasks(task_list):
    prompt = f"Prioritize these tasks based on urgency and importance:\n{task_list}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a productivity assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)
