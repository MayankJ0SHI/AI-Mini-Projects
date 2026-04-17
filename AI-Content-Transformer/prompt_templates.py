from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.load import loads, dumps
import os

teacher_examples = [
    {
        "input": "Explain APIs",
        "output": "Think of an API like a waiter in a restaurant. You place an order, waiter takes it to kitchen, and brings response back."
    },
    {
        "input": "What is a database?",
        "output": "A database is like a digital notebook where data is stored and retrieved whenever needed."
    }
]

blogger_examples = [
    {
        "input": "Explain APIs",
        "output": (
            "Title: Understanding APIs\n\n"
            "Introduction: APIs allow communication between systems...\n\n"
            "How it works:\n"
            "1. Request\n"
            "2. Processing\n"
            "3. Response\n\n"
            "Conclusion: APIs power modern apps."
        )
    },
    {
        "input": "What is machine learning?",
        "output": (
            "Title: Machine Learning Explained\n\n"
            "Introduction: ML enables systems to learn from data...\n\n"
            "Applications: recommendations, fraud detection, etc."
        )
    }
]

social_media_writer_examples = [
    {
        "input": "Explain APIs",
        "output": (
            "1/ APIs power the internet.\n"
            "2/ Think of them as waiters.\n"
            "3/ Request → API → Server\n"
            "4/ Response comes back.\n"
            "5/ Used in almost every app."
        )
    },
    {
        "input": "What is AI?",
        "output": (
            "1/ AI = Artificial Intelligence 🤖\n"
            "2/ Machines that think like humans\n"
            "3/ Used in Netflix, Google, cars\n"
            "4/ Learns from data\n"
            "5/ The future of tech"
        )
    }
]

base_example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="""
Input: {input}
Output: {output}
"""
)

def ai_content_transformer_template(promptRole: str):
    promptRole = promptRole.lower()

    if promptRole == "blogger":
        prompt_template = FewShotPromptTemplate(
            examples=blogger_examples,
            example_prompt=base_example_prompt,
            prefix="""
You are a professional blog writer.

Task:
Convert the input into a well-structured blog post with headings, intro, and conclusion.
""",
            suffix="""
Input: {input}
Output:
""",
            input_variables=["input"]
        )

    elif promptRole == "teacher":
        prompt_template = FewShotPromptTemplate(
            examples=teacher_examples,
            example_prompt=base_example_prompt,
            prefix="""
You are a friendly teacher explaining concepts to beginners.

Explain the topic using:
- Simple language
- Analogies
- Step-by-step breakdown
""",
            suffix="""
Input: {input}
Output:
""",
            input_variables=["input"]
        )

    elif promptRole == "social media writer":
        prompt_template = FewShotPromptTemplate(
            examples=social_media_writer_examples,
            example_prompt=base_example_prompt,
            prefix="""
You are a viral social media content creator.

Convert the input into a Twitter thread:
- Hook in first line
- Numbered tweets
- Engaging tone
""",
            suffix="""
Input: {input}
Output:
""",
            input_variables=["input"]
        )

    else:
        raise ValueError(
            "Invalid Role provided. Provide: blogger, teacher, or social media writer"
        )

    return prompt_template

def save_prompt(role: str):
    os.makedirs('saved_prompts', exist_ok=True)
    save_path = os.path.join('saved_prompts',f"{role}.json")
    prompt_template = ai_content_transformer_template(role)
    with open(save_path,'w') as f:
        f.write(dumps(prompt_template))
    print("✅ Saved prompt for role {role} successfully.")

def load_prompt(role: str):
    save_path = os.path.join('saved_prompts',f"{role}.json")
    with open(save_path,'r') as f:
        data = f.read()
    prompt = loads(data)
    print("✅ Loaded prompt for role {role} successfully.")
    return prompt
    