from dotenv import load_dotenv
import os
from google import genai
from rich.console import Console
from prompts import generate_coding_coach_prompt

console = Console()

# Load API key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise Exception("Set GOOGLE_API_KEY in your .env file")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

def ask_coding_coach(task_description: str) -> str:
    """Send task to coding coach LLM and return structured guidance"""
    prompt = generate_coding_coach_prompt(task_description)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    console.print("[bold green]Welcome to your Coding Coach![/bold green]")
    task = input("Describe the coding task you want guidance on:\n")
    guidance = ask_coding_coach(task)
    console.print(guidance)