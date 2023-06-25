# gpt4web.py

# imports
import os # for working with venv vars and pathes
import openai  # for calling the OpenAI API
import time # for the logs

# models
GPT_MODEL = "gpt-4"
# openai.organization = ""
openai.api_key = os.getenv("OPENAI_API_KEY")

conversation_history = [
    {'role': 'system', 'content': 'You are a helpful assistant'},
]

def generate_response(query):
    conversation_history.append({'role': 'user', 'content': query})
    response = openai.ChatCompletion.create(
        messages=conversation_history,
        model=GPT_MODEL,
        temperature=0,
    )
    generated_response = response['choices'][0]['message']['content']
    conversation_history.append({'role': 'assistant', 'content': generated_response})

    # Create a directory named 'logs' if it doesn't already exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Create a unique filename using the current timestamp
    filename = f"logs/conversation_history_{int(time.time())}.txt"

    # Save conversation history to a file
    with open(filename, "w") as f:
        for message in conversation_history:
            f.write(f"{message['role']}: {message['content']}\n")

    return generated_response
