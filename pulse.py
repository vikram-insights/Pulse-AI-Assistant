import ai_utils
from colorama import Fore, Style, init
import os
from datetime import datetime
import json

init()


def ask_ai(message, history):
    # 1. Send the user message to the AI utility
    success, result = ai_utils.chat_with_ai(message, history)

    # 2. Return the AI response or error result
    return success, result


def start_ai_chat():
    print("Type 'exit' anytime to end the conversation.")
    history = []

    while True:
        print("-" * 70)

        # 1. Get the message from the user
        message = input(Fore.CYAN + "You 👤 : " + Style.RESET_ALL) 

        # 2. Pusle Commands
        command = message.strip().lower()
        if command == "/clear":
            history.clear()
            print("🧹 Conversation history cleared.")
            continue

        elif command == "exit":
            print("👋 Ending conversation...")
            break

        elif command == "/help":
            print("""
        Available Commands:

        /clear - Clear the conversation history
        /help  - Show available commands
        exit   - Exit conversation
        /save  - Save conversation
                   
        """)
            continue

        elif command == "/history":
            print("\n📃 Conversation History")
            

            if not history:
                print("No conversation history yet")
            else:
                for index, convo in enumerate(history, start=1):
                    user_message = convo["user"]
                    assistant_response = convo["assistant"]
                    preview = assistant_response[:80]
                    print(f"\n{index}. You : {user_message}")
                    print(f"  Pulse : {preview}...")
            continue

        elif command == "/save":
            success, result = save_conversation(history)
            print(f"Saved 💾 : {result}")
            continue

        # 3. Send the message to the AI
        success, result = ask_ai(message, history)

        if success:
            history.append({
                "user" : message,
                "assistant" : result
            })
        else:
            print(Fore.RED + result + Style.RESET_ALL)


def save_conversation(history):
    try:
        today = datetime.now()
        file_name = today.strftime("%d_%m_%Y_%H_%M_%S")
        actual_filename = "conversation_" + file_name + ".json"
        os.makedirs("Conversation", exist_ok=True)
        file_path = os.path.join("Conversation", actual_filename)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)


        return True, actual_filename

    except Exception as e:
        return False, f"Save Error: {e}"
