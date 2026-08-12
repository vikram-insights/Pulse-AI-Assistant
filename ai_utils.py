from google import genai
from config import GEMINI_API_KEY
from validation import check_empty_string
from google.genai import types
from prompts import PULSE_INSTRUCTIONS

client = genai.Client(api_key=GEMINI_API_KEY)


# ? BASIC AI CHAT
def chat_with_ai(message, history):
    conversation = []
    # 1. Validate user message
    input_success, input_result = check_empty_string(message=message)
    if not input_success:
        return False, input_result

    try:
        for convo in history:
            conversation.append({
                "role" : "user",
                "parts" : [{"text" : convo["user"]}]
            })

            conversation.append({
                "role" : "model",
                "parts" : [{"text" : convo["assistant"]}]
            })

        conversation.append({
            "role" : "user",
            "parts" : [{"text" : message}]
        })

        # 2. Semd the message to Gemini and Generate a response
        thinking = "Pulse 🤖 : Thinking..."
        print(thinking, end="", flush=True)
        response = client.models.generate_content_stream (
            model="gemini-3.6-flash",
            contents=conversation,
            config=types.GenerateContentConfig(
    system_instruction=PULSE_INSTRUCTIONS))

        ai_response = ""
        first_chunk = True
        for chunk in response:
            if first_chunk:
                # Handles thinking....
                print("\r" + " " * len(thinking) + "\r", end="")
                print("Pulse 🤖 : ", end="", flush=True)
                first_chunk = False
            print(chunk.text, end="")
            ai_response += chunk.text
        print()

        # 3. Return the generated AI response
        return True, ai_response

    except Exception as e:
        # 4. Handle any API or unexpected error
        return False, f"AI Error: {e}"
