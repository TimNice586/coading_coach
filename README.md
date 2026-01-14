# Coding Coach — Interactive LLM Assistant for Coding Guidance

## Project Overview  
Coding Coach is an interactive Python application that leverages the Google Gemini AI model to provide step-by-step coding guidance based on user prompts.  
It allows users to:

- Submit a coding task or question
- Receive detailed explanations, code suggestions, and best practices
- Automatically save each prompt and response for later reference

The goal is to provide a personal coding assistant that can help accelerate learning, solve coding problems, and track progress over time.

🎯 Key Objectives

- **Interactive Assistance** – Ask any coding question and get structured guidance  
- **Output Saving** – Automatically save all user prompts and AI responses in timestamped text files  
- **Reproducibility** – Keep a historical record of prompts/responses for future reference  
- **Ease of Use** – Simple CLI-based interface with minimal setup  

🤖 Technology & Models Used

- **Google Gemini 2.5 Flash** via `genai` Python SDK  
- **Python 3.10+** for scripting and file handling  
- **Rich** library for colored console outputs  
- **dotenv** for API key management  

🔍 Technical Highlights

🔧 **Data Handling & Output Saving**  
- Each prompt/response pair is stored in a timestamped `.txt` file in `outputs/`  
- Folder is automatically created if missing  
- Easy to review or use for later analysis  

📈 **Interactive Workflow**  
- CLI-based input loop  
- Type multiple prompts in one session  
- Exit with `exit` or `quit`  

📦 **Project Structure**


├── outputs/ # Automatically created folder for saved prompts/responses

├── prompts.py # Contains prompt templates and helper functions

├── coach_main.py # Main interactive script for Coding Coach

├── README.md # Project overview and instructions

├── requirements.txt # Python dependencies

└── .env # Contains GOOGLE_API_KEY

markdown
Copy code

🚀 **How to Run**

1. Install dependencies:
```bash
pip install -r requirements.txt
Set your Google API key in .env:

ini
Copy code
GOOGLE_API_KEY=your_api_key_here
Run the interactive coding coach:

Copy code
python coach_main.py
Enter your coding questions or tasks in the prompt

Responses are displayed in the console and automatically saved in outputs/

```

## Timeline
This project was implemented in one hour as a personal coding assistant prototype, focusing on AI interaction, output saving, and CLI usability.

## 👤 Author

Tim De Nijs

Data Science & AI — BeCode Ghent (2025–2026)