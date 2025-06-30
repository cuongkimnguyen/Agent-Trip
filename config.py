import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")  # "groq" or "openai"
MODEL_NAME = os.getenv("MODEL_NAME")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
