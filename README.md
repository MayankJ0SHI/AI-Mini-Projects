# AI-Mini-Projects

This repository is a collection of small yet impactful AI projects. Each folder contains a self-contained project, its code, and necessary setup instructions.

---

## Projects

### 1. AI-Decision-Assistant

An interactive assistant that helps you make better decisions using the power of AI language models and predefined personas (Coach, Manager, Friend). You pose a career or life question and receive responses in the style of different helpful perspectives.

**Features:**
- Provides career advice from unique "personas" (Coach, Manager, Friend), each with their own mindset and tone.
- Leverages Language Model APIs for generating high-quality, context-aware suggestions.
- Saves decision prompts for future reference or analysis.
- Simple command-line interface.
- Flexible prompt template system.

**How it Works:**
- You run the program and supply a question.
- The assistant displays each persona's approach.
- It generates and prints prompts, runs them through your chosen AI model (as set up in `llm_factory.py`), and returns answers from each perspective.
- Prompts are saved for traceability or auditing.

**Setup & Usage:**

1. **Clone this repository:**
    ```sh
    git clone https://github.com/MayankJ0SHI/AI-Mini-Projects.git
    cd AI-Mini-Projects/AI-Decision-Assistant
    ```

2. **Create & activate a Python virtual environment (optional but recommended):**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
    The main dependencies (from `requirements.txt`) are:
    - `langchain`
    - `langchain-openai`
    - `langchain-google-genai`
    - `python-dotenv`

4. **Configure API Keys:**
    - Some LLM integrations (e.g., OpenAI, Google Generative AI) require API keys. Check and edit `config.json` to input your keys as needed. See the relevant LLM in `llm_factory.py` for details.

5. **Run the Project:**
    ```sh
    python app.py
    ```
    You'll be asked to input your decision question and will receive responses from all personas.

**File Structure:**
```
AI-Decision-Assistant/
├── app.py                    # Main CLI application
├── descision_assistant_prompt_generator.py  # Prompt generator logic
├── llm_factory.py            # Pluggable Language Model API integration
├── requirements.txt          # Python dependencies
├── config.json               # API key/config file
├── saved_prompt/             # Saved prompt templates
```

---

## Adding More Projects

Each new folder should:
- Contain its own code and dependencies.
- Have similar sections in this README: **What it does, Features, How to Run, Setup**.

If you add another project, adjust this README in the same fashion.

---

## License

This repository is open-source. Feel free to fork, contribute, or raise issues.
