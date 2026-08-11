from google import genai
from config import GEMINI_API_KEY
from validation import check_empty_string

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
        response = client.models.generate_content(
            model="gemini-3.6-flash", contents=conversation
        )
        # 3. Return the generated AI response
        return True, response.text

    except Exception as e:
        # 4. Handle any API or unexpected error
        return False, f"AI Error: {e}"


