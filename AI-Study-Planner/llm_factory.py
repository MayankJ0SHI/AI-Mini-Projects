import os
import json
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

with open('config.json','r') as f:
    config = json.load(f)
provider=config['provider']

def get_llm():
    if provider=='openai':
        llm = ChatOpenAI(
            model=config[provider]['model'],
            max_tokens=config[provider]['max_tokens'],
            temperature=config[provider]['temperature']
        )
    elif provider=='gemini':
        llm = ChatGoogleGenerativeAI(
            model=config[provider]['model'],
            max_tokens=config[provider]['max_tokens'],
            temperature=config[provider]['temperature']
        )
    else:
        raise ValueError("❌ Invalid provider name in the config file.[Provide either openai or gemini]")
    return llm