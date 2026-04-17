import os
os.environ["GRPC_VERBOSITY"]="NONE"
os.environ["GLOG_minloglevel"]="3"#FATAL

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.load import dumps,loads

def get_decision_assistant_prompt_template():
    decision_assistant_prompt = ChatPromptTemplate.from_messages([
        ("system", """
You are an AI decision assistant.

Use the following personas:
{personas}

For each persona:
- Think carefully and analyze all paths
- Provide exactly 3 reasoning points
- Then give advice

Each persona MUST have a different perspective.

Follow this strict format:

[Coach]
Reasoning:
- ...
- ...
- ...
Advice:
...

[Manager]
Reasoning:
- ...
- ...
- ...
Advice:
...

[Friend]
Reasoning:
- ...
- ...
- ...
Advice:
...

[Final Decision]
Summary:
...
Final Recommendation:
...
"""),
        ("human", "Decision: {question}")
    ])
    return decision_assistant_prompt

def generate_prompt(personas, question):
    
    decision_assistant_prompt = get_decision_assistant_prompt_template()
    formatted_prompt = decision_assistant_prompt.format_messages(personas=personas, question=question)
    return formatted_prompt

def save_prompt_template():
    decision_assistant_prompt = get_decision_assistant_prompt_template()
    save_dir = "saved_prompt"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join('saved_prompt','decision_assistant_prompt_template.json')
    with open(save_path, 'w') as f:
        f.write(dumps(decision_assistant_prompt))
    print('✅ Decision Assistant Prompt Template Saved Successfully.')

def load_prompt_template(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Prompt file not found: {path}")
    with open(path, "r") as f:
        data = f.read()
    prompt = loads(data)
    print('✅ Prompt loaded successfully.')
    return prompt