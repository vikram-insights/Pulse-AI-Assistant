from google import genai
from config import GEMINI_API_KEY
from validation import check_empty_string

client = genai.Client(api_key=GEMINI_API_KEY)


# ? BASIC AI CHAT
def chat_with_ai(message):
    # 1. Check empty string
    input_success, input_result = check_empty_string(message=message)
    if not input_success:
        return False, input_result
    
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash", contents=message
        )

        return True, response.text

    except Exception as e:
        return False, f"AI Error: {e}"


if __name__ == "__main__":
    success, result = chat_with_ai("Hello! Introduce yourself.")

    if success:
        print(result)
    else:
        print(result)
