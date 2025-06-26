from agents.assistant_agent import AssistantAgent

def main():
    agent = AssistantAgent()
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            break
        response = agent.run(user_input)
        print("Assistant:", response)

if __name__ == "__main__":
    main()
