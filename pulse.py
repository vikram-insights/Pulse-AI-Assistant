import ai_utils



def ask_ai(message):
    success, result = ai_utils.chat_with_ai(message)
    return success, result
    



