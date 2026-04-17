from llm_factory import get_llm
from prompt_templates import ai_content_transformer_template,save_prompt

def main():
    print("\n===== 👾 AI Content Transformer =====\n")

    print("\n===== Select Role =====\n")
    print("1. 😎 blogger\n")
    print("2. 🧑‍🏫 teacher\n")
    print("3. 😇 social media writer\n")

    role = str(input('Enter your role: ').strip().lower())
    content = str(input('Enter your content: ').strip())
    
    try:
        prompt_template = ai_content_transformer_template(role)
        print(f"\n===== 🤖 Prompt Template for {role} =====\n")
        print(prompt_template)
        
        formatted_prompt_template = prompt_template.format(input=content)
        print(f"\n===== 🤖 Prompt for {role} =====\n")
        print(formatted_prompt_template)
        
        llm = get_llm()
        print(f"\n===== 🤖 Model being used {type(llm).__name__} =====\n")
        
        response = llm.invoke(formatted_prompt_template)
        print(f"===== 🤖 Model's Prediction  =====")
        print(response.content)
        
        print("\n===== 🤖 Saved the prompt for role {role} =====\n")
        save_prompt(role)
        
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == '__main__':
    main()