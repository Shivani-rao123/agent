import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load task list from file
def read_tasks(filepath):
    with open(filepath, 'r') as f:
        return f.read()

# Summarize the tasks into categories
def summarize_tasks(tasks):
    model = genai.GenerativeModel("models/gemini-1.5-flash")

    prompt = f"""
You are a smart task planning agent.

Categorize these tasks into priority levels.

Tasks:
{tasks}

Return the response exactly like this (do not rename tasks):
High priority:
- task 1
- task 2
Medium priority:
- task 3
- task 4
Low priority:
- task 5
- task 6
"""

    response = model.generate_content(prompt)
    return response.text

# Run the program
if __name__ == "__main__":
    task_text = read_tasks("tasks.txt")
    summary = summarize_tasks(task_text)
    print("\nTask summary:\n")
    print("_" * 30)
    print(summary)
