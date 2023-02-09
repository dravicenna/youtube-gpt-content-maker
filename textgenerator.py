import os

import openai
from dotenv import load_dotenv

from config import API_PARAM, PROMPT_TEMPLATE

load_dotenv()  # take environment variables from .env.

# Define the API key
openai.api_key = os.getenv('OPENAI_TOKEN')


def clean_response(text: str) -> list[str]:
    text = text.strip().strip('[]').split('\n')
    return [t.strip().strip(',').strip('"') for t in text]


def generate_text_list(date: str) -> str:
    # Define the prompt for the API request
    prompt = PROMPT_TEMPLATE + date + ":"

    # Make the API request
    response = openai.Completion.create(
        prompt=prompt,
        **API_PARAM
    )

    # Extract the generated text
    generated_text = response["choices"][0]["text"]

    return clean_response(generated_text)
