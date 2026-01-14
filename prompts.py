def generate_coding_coach_prompt(task_description: str) -> str:
    """
    Generates a detailed prompt for the coding coach LLM.
    Includes instructions to produce step-by-step guidance with code,
    explanations, examples, improvements, and intermediate steps.
    """
    return f"""
You are a professional Python coding coach. The student wants to complete this task:

TASK: {task_description}

Provide a step-by-step plan for solving it. For each step:
1. Give the Python code (efficient, modular, include #comments)
2. Explain what the code does and why
3. Explain how to do this step solo (research, documentation, StackOverflow)
4. Provide example outputs if applicable
5. Show how this step fits in the overall solution
6. Suggest improvements or best practices
7. Mention any intermediate steps (e.g., install packages)
8. Specify file name and placement for each code snippet

Format response clearly with numbered steps and headers.
"""