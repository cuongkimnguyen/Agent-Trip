from langchain_community.chat_models import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

class GroqClient:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model_name=MODEL_NAME,
            temperature=0.7,
        )

    def chat(self, prompt: str) -> str:
        return self.llm.predict(prompt).strip()
