import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")