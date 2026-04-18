from langchain_core.load import loads, dumps
import os

PROMPT_SAVE_DIR = "saved_prompts"

def get_prompt_save_path(filename: str):
    os.makedirs(PROMPT_SAVE_DIR, exist_ok=True)
    return os.path.join(PROMPT_SAVE_DIR, filename)

def save_prompt(prompt, filename: str):
    path = get_prompt_save_path(filename)
    with open(path, "w") as f:
        f.write(dumps(prompt))

def load_prompt(filename: str):
    path = get_prompt_save_path(filename)
    with open(path, "r") as f:
        return loads(f.read())