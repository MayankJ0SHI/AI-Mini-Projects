from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from examples.study_plan_example import study_planner_examples
from output_parsers.study_plan_parser import get_study_plan_parser

def build_study_plan_prompt():
    parser = get_study_plan_parser()
    format_instructions = parser.get_format_instructions()

    example_prompt = PromptTemplate(
        input_variables=['goal','duration','output'],
        template="""
Goal: {{goal}}

Duration: {{duration}}

Output:
{{output}}
""",
        template_format="jinja2"
    )

    prompt = FewShotPromptTemplate(
        examples=study_planner_examples,
        example_prompt=example_prompt,
        input_variables=['goal','duration'],
        partial_variables={'format_instructions': format_instructions},

        prefix="""
You are an Expert Teacher and curriculum designer.

Your task is to create structured, day-wise study plans.

Guidelines:
- Start from basics → advanced
- Keep it realistic
- Cover all days

{{format_instructions}}
""",

        suffix="""
Goal: {{goal}}

Duration: {{duration}}

Output:
""",

        template_format="jinja2"  # 🔥 IMPORTANT
    )

    return prompt