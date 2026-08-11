def ask_ai(message):
    # 1. Send the user message to the AI utility
    success, result = ai_utils.chat_with_ai(message)

    # 2. Return the AI response or error result
    return success, result


def start_ai_chat():
    print("Type 'exit' anytime to end the conversation.")
    history = []
    while True:
        print("-" * 70)
        print("-" * 20)
        # 1. Get the message from the user
        message = input("You 👤 : ") 

        # 2. Exit the conversation if user types 'exit'
        if message.strip().lower() == "exit":
            print("👋 Ending conversation...")
            break

        # 3. Send the message to the AI
        success, result = ask_ai(message)

        history.append({
            "user" : message,
            "pulse" : result
        })

        # 4. Display the AI response
        print(f"Pulse 🤖 : {history}")


start_ai_chat()
