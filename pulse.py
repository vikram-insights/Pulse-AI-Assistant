import ai_utils
from colorama import Fore, Style, init
import os
from datetime import datetime
import json
from validation import check_empty_string

init()


def ask_ai(message, history):
    # 1. Send the user message to the AI utility
    success, result = ai_utils.chat_with_ai(message, history)

    # 2. Return the AI response or error result
    return success, result


def start_ai_chat():
    print("Type 'exit' anytime to end the conversation.")
    history = []

    # 1. Handle Pulse commands
    while True:
        print("-" * 70)

        # 2. Get the message from the user
        message = input(Fore.CYAN + "You 👤 : " + Style.RESET_ALL) 

        command = message.strip().lower()

        if command == "/clear":
            confirmation = input("Are you sure? (y/n) : ").strip().lower()
            success, result = check_empty_string(confirmation=confirmation)
            if not success:
                print(result)
                continue

            if confirmation == "y":
                history.clear()
                print("🧹 Conversation history cleared.")
            elif confirmation == "n":
                print("Cancelled.")
            else:
                print("Invalid confirmation input!")
            continue

        elif command == "exit":
            print("👋 Ending conversation...")
            break

        elif command == "/help":
            print("""
        Available Commands:

        /clear - Clear the conversation history
        /help  - Show available commands
        /history - Show conversation history
        /exit   - Exit conversation
        /save  - Save conversation
        /load  - Load the selected conversation
        /delete - Delete the conversation file
        /count - Show conversation exchange count
        /search - Search conversation using keyword
        /last  - Load the selected conversation
        /stats - Show the current active conversation stats
                   
        """)
            continue

        elif command == "/history":
            print("\n📃 Conversation History")
            

            if not history:
                print("No conversation history yet")
                continue

            for index, convo in enumerate(history, start=1):
                preview = convo["assistant"][:80]
                print(f"\n{index}. You : {convo['user']}")
                print(f"  Pulse : {preview}...")
            continue


        elif command == "/save":
            success, result = save_conversation(history)
            if success:
                print("Conversation saved successfully.")
            else:
                print(result)
            continue

        elif command == "/load":
            success, result = load_conversation()
            if success:
                history = result
                print("Conversation loaded successfully.")
            else:
                print(result)
            continue

        elif command == "/delete":
            success, result = delete_conversation()
            print(result)
            continue

        elif command == "/count":
            print(f"Conversation exchanges: {len(history)}")
            continue

        elif command == "/search":

            found = False

            # 1. Get the input from the user
            search_term = input("Enter keyword: ").strip().lower()

            # 2. Validate the input
            success, result = check_empty_string(search_term=search_term)
            if not success:
                print(result)
                continue

            print(f"\n🔍 Search results for: {search_term}")

            # 3. Get all saved conversation files
            for filename in os.listdir("Conversation"):
                if not filename.endswith(".json"):
                    continue

                file_path = os.path.join("Conversation", filename)

                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        saved_history = json.load(file)

                    # 4. Search inside the conversation
                    for chat in saved_history:
                        if (
                            search_term in chat["user"].lower()
                            or search_term in chat["assistant"].lower()
                        ):
                            
                            print(f"You    : {chat['user']}")
                            print(f"Pulse  : {chat['assistant']}")
                            found = True

                except (FileNotFoundError, json.JSONDecodeError):
                    continue

            # 5. Display result status
            if not found:
                print("No conversation found with this keyword!")

            continue


        elif command == "/export":
            success, result = export_conversation(history)
            if success:
                print(f"Conversation exported successfully: {result}")
            else:
                print(result)
            continue

                
        elif command == "/last":
            if history:
                print(history[-1]["user"])
                print(history[-1]["assistant"])
            else:
                print("No conversation found!")
            continue


        elif command == "/stats":
            user_words = 0
            assistant_words = 0

            for chat in history:
                user_words += len(chat["user"].split())
                assistant_words += len(chat["assistant"].split())

            total_words = user_words + assistant_words

            print("\n📊 Conversation Stats")
            print("-" * 30)
            print(f"Exchanges       : {len(history)}")
            print(f"User words      : {user_words}")
            print(f"Pulse words     : {assistant_words}")
            print(f"Total words     : {total_words}")

            continue


        elif command == "/about":
            print("🤖 Pulse AI Assistant")
            print("Version   : 1.2")
            print("Language  : Python")
            print("AI Model  : Gemini")
            print("Developer : Vikram") 
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
        # 1. Generate a unique filename using the current date and time
        actual_filename = (
            "conversation_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".json"
        )

        # 2. Create the Conversation folder if doesn't exist
        os.makedirs("Conversation", exist_ok=True)
        file_path = os.path.join("Conversation", actual_filename)

        # 3. Save the conversation history as JSON
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

        return True, actual_filename

    except Exception as e:
        return False, f"Save Error: {e}"


def export_conversation(history):
    
    # 1. Generate a unique filename using the current date and time
    actual_filename = (
        "Exports_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    )

    try:
        # 2. Create the Conversation folder if it doesn't exist
        os.makedirs("Exports", exist_ok=True)
        file_path = os.path.join("Exports", actual_filename)

        # 3. Save the conversation history as text
        with open(file_path, "w", encoding="utf-8") as file:
            for chat in history:
                file.write(f"You : {chat['user']}\n")
                file.write(f"Pulse : {chat['assistant']}\n\n")

        # 4. Return the export result
        return True, actual_filename

    except Exception as e:
        return False, f"Export Error: {e}"
    


def load_conversation():
    # 1. Get saved conversation files
    new_history = []
    for history in os.listdir("Conversation"):
        if history.endswith(".json"):
            new_history.append(history)
        
    if not new_history:
        return False, "No saved conversation found."
    
    # 2. Display available conversations and get user selection
    for index, history in enumerate(new_history, start=1):
        print(f"{index}. {history}")

    try:
        number = int(input("Enter file number: "))
    except ValueError:
        return False, "Invalid input!"

    if number < 1 or number > len(new_history):
        return False, "Invalid selection!"

        
    # 3. Load selected conversation   
    selected_file = new_history[number-1]

    try:
        file_path = os.path.join("Conversation", selected_file)
        with open(file_path, "r", encoding="utf-8") as file:
            loaded_history = json.load(file)
            return True, loaded_history
    except FileNotFoundError:
        return False, "File not found with selected number"




def delete_conversation():
    # 1. Get saved conversation files
    new_history = []
    for history in os.listdir("Conversation"):
        if history.endswith(".json"):
            new_history.append(history)
        
    if not new_history:
        return False, "No saved conversation found."
    
    # 2. Display available conversations and get user selection
    for index, history in enumerate(new_history, start=1):
        print(f"{index}. {history}")

    try:
        number = int(input("Enter file number: "))
    except ValueError:
        return False, "Invalid input!"

    if number < 1 or number > len(new_history):
        return False, "Invalid selection!"

        
    # 3. Delete selected conversation   
    selected_file = new_history[number - 1]

    try:
        file_path = os.path.join("Conversation", selected_file)
        os.remove(file_path)
        return True, "File deleted successfully."
    except FileNotFoundError:
        return False, "File not found with selected number"

