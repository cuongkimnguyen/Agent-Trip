from config import MODEL_PROVIDER

def create_client():
    if MODEL_PROVIDER == "openai":
        from services.openai_client import OpenAIClient
        return OpenAIClient()
    elif MODEL_PROVIDER == "groq":
        from services.groq_client import GroqClient
        return GroqClient()
    else:
        raise ValueError(f"Unsupported MODEL_PROVIDER: {MODEL_PROVIDER}")
