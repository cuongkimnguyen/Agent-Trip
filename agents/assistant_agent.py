from services.openai_client import OpenAIClient
from utils.text_utils import load_prompt_template
from services.client_factory import create_client

class AssistantAgent:
    def __init__(self):
        print("Importing AssistantAgent...")
        self.client = create_client()
        self.base_prompt = load_prompt_template("prompts/base_prompt.md")

    def run(self, user_input: str) -> str:
        prompt = self.base_prompt.format(user_input=user_input)
        return self.client.chat(prompt)
