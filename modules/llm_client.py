import os
import openai

def call_llm(prompt: str, model: str = 'gpt-4') -> str:
    api_key = os.getenv('OPENAI_API_KEY')
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
                  {'role': 'user', 'content': prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()
