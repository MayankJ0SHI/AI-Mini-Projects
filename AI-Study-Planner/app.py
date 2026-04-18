from llm_factory import get_llm
from prompts.study_planner_prompt_builder import build_study_plan_prompt
from output_parsers.study_plan_parser import get_study_plan_parser

def main():
    print("\n🚀 AI Study Planner - Execution Started\n")
    savefileName = 'study_plan_prompt.json'
    # =========================
    # Step 1: Build Prompt
    # =========================
    print("🔧 Building prompt template...")
    prompt = build_study_plan_prompt()

    # =========================
    # Step 2: User Input
    # =========================
    goal = input("\n🎯 Enter your learning goal: ").strip()
    duration = input("⏳ Enter duration (e.g., 7 days): ").strip()

    if not goal or not duration:
        print("❌ Goal and Duration cannot be empty.")
        return

    formatted_prompt = prompt.format(goal=goal, duration=duration)

    # =========================
    # Step 3: LLM Invocation
    # =========================
    print("\n🤖 Generating study plan using LLM: ...")
    llm = get_llm()
    raw_response = llm.invoke(formatted_prompt)

    response = raw_response.content

    # =========================
    # Step 4: Parse Response
    # =========================
    print("🧠 Parsing structured output...")
    parser = get_study_plan_parser()

    try:
        parsed_response = parser.parse(response)
    except Exception as e:
        print("❌ Failed to parse response.")
        print("Raw Output:\n", response)
        print("Error:", e)
        return

    # =========================
    # Step 5: Display Output
    # =========================
    print("\n✅ Study Plan Generated Successfully!\n")
    print(f"📌 Goal: {parsed_response.goal}")
    print(f"📅 Duration: {parsed_response.duration}\n")

    for day in parsed_response.plan:
        print(f"📖 Day {day.day} ({day.difficulty})")
        for topic in day.topics:
            print(f"   • {topic}")
        print()

    print("🎉 Done!\n")


if __name__ == '__main__':
    main()