#!/usr/bin/env python3
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

def get_repo_path():
    try:
        if len(sys.argv) > 1:
            git_repo_path = sys.argv[1]
            if os.path.exists(git_repo_path) and os.path.isdir(git_repo_path):
                return git_repo_path
            else:
                print(
                    f"Error: Path '{git_repo_path}' does not exist or is not a directory"
                )
                sys.exit(1)
        else:
            # Use current directory if no path provided
            return os.getcwd()
    except Exception as e:
        print(f"Error getting repo path: {e}")
        sys.exit(1)


repo_path = get_repo_path()
print(f"Using git repo path: {repo_path}")

# Change to the repository directory
os.chdir(repo_path)


def get_git_diff():
    # Check if we're in a git repository
    if (
        not os.path.exists(".git")
        and subprocess.run(
            "git rev-parse --git-dir", capture_output=True, shell=True
        ).returncode
        != 0
    ):
        print("Error: Not a git repository")
        sys.exit(1)

    # Get staged changes (cached diff)
    output = subprocess.run(
        "git diff --cached", capture_output=True, shell=True, text=True
    )

    if output.returncode != 0:
        print(f"Error running git diff: {output.stderr}")
        sys.exit(1)

    if not output.stdout.strip():
        print(
            "No staged changes found. Please stage your changes with 'git add' first."
        )
        sys.exit(1)

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

try:
    response = model.invoke(commit_prompt)
    print(response.content)
except Exception as e:
    print(f"Error generating commit message: {e}")
    sys.exit(1)