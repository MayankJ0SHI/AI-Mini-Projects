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

### 2. AI Content Transformers

A modular toolset for transforming content using AI models. It enables tasks such as rewriting, summarizing, translating, and adapting text between styles, all powered by pluggable language model APIs.

**Features:**
- Flexible transformations: rewrite, summarize, translate, and re-style content for different audiences or tones.
- Easily extensible – add new transformation templates or target formats.
- Integrates with multiple Language Model APIs for powerful text processing.
- Batch processing support for multiple documents at once.
- Command-line interface for quick use and automation.

**How it Works:**
- You supply the original content and select a transformation type (e.g., summarize, rewrite as formal, translate).
- The tool constructs the appropriate prompt and sends it to the configured AI model (see `llm_factory.py` for supported backends).
- Transformed content is displayed and optionally saved to output files.
- You can add or customize transformation templates as needed.

**Setup & Usage:**

1. **Clone this repository:**
    ```sh
    git clone https://github.com/MayankJ0SHI/AI-Mini-Projects.git
    cd AI-Mini-Projects/AI-Content-Transformers
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
    - Some LLM integrations (e.g., OpenAI, Google Generative AI) require API keys. Edit `config.json` to input your keys as needed. For detailed LLM usage, refer to the backend code in `llm_factory.py`.

5. **Run the Project:**
    ```sh
    python transformer.py
    ```
    You will be prompted to provide your content and select a transformation. The transformed result will be printed or saved as specified.

**File Structure:**
```
AI-Content-Transformers/
├── transformer.py                # Main CLI application
├── content_transformer_templates.py  # Transformation template logic
├── llm_factory.py                # Pluggable Language Model API integration
├── requirements.txt              # Python dependencies
├── config.json                   # API key/config file
├── outputs/                      # Saved transformed outputs
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
