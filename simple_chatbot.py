# simple_chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "what's your name": "I'm a simple Python chatbot!",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome!",
        "who created you": "I was created by a Python developer."
    }

    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]

    return "I'm not sure how to respond to that."


def main():
    print("🤖 Chatbot: Hello! I'm your Python chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() == "bye":
            print("🤖 Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"🤖 Chatbot: {response}")


if __name__ == "__main__":
    main()
