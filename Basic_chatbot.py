def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I'm not sure I understand. Could you rephrase?"

print("🤖 Chatbot: Hi! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("🤖 Chatbot:", chatbot_response(user_input))
        break
    response = chatbot_response(user_input)
    print("🤖 Chatbot:", response)

