from google import generativeai as genai

def start_recipe_chat():
    """Start a new Gemini chat session."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    return model.start_chat()

def get_recipe_response(chat, prompt: str) -> str:
    """Send prompt to Gemini chat and return the response."""
    response = chat.send_message(prompt)
    return response.text.strip()
