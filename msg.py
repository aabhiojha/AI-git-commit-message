import getpass
import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")


model = init_chat_model("llama3-8b-8192", model_provider="groq")
response = model.invoke("Hello, world!")

print(response.content)
