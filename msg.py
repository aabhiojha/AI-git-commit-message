import getpass
import os
import subprocess
import sys

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

model = init_chat_model("llama3-8b-8192", model_provider="groq")

print(
    """
    Example usage: 
    python msg.py optional:path/to/git_repo
    
"""
)


def get_repo_path():
    try:
        git_repo_path = sys.argv[1]
        if os.path.exists(git_repo_path):
            print("The command is invoked from within a git directory")
    except:
        print("Give valid path")


def get_git_diff():
    output = subprocess.run("git diff", capture_output=True, shell=True, text=True)
    return output.stdout


changes = get_git_diff()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            (
                """
                You are an expert in writing clear, conventional git commit messages. 
                Your task is to generate a single, well-formatted commit message based on the user's input. 
                Follow these rules:\n
                - Use the Conventional Commit style (e.g., feat:, fix:, docs:, refactor:)\n
                - Write in the imperative mood (e.g., 'add feature', not 'added feature')\n
                - Keep the message concise and under 50 characters for the summary\n
                - Do not include explanations, only output the commit message text
                """
            ),
        ),
        ("human", "{changes}"),
    ]
)
commit_prompt = prompt.format_messages(changes=changes)

reponse = model.invoke(commit_prompt)

print(reponse.content)
