import ai_utils
from colorama import Fore, Style, init

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

        # 2. Exit the conversation if user types 'exit'
        if message.strip().lower() == "exit":
            print("👋 Ending conversation...")
            break

        # 3. Send the message to the AI
        success, result = ask_ai(message, history)

        if success:
            history.append({
                "user" : message,
                "assistant" : result
            })
        else:
            print(Fore.RED + result + Style.RESET_ALL)

