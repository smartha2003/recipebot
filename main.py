from google import generativeai as genai
from chat_utils import start_recipe_chat, get_recipe_response
from prompts import format_prompt

genai.configure(api_key="AIzaSyDHnIXoQisf0mSYTAas7inr1Q54isYLTc0")

chat = start_recipe_chat()

print("🍽️  Welcome to RecipeBot! Ask me for a recipe. Type 'exit' to quit.")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'exit':
        print("Goodbye! 👋")
        break

    prompt = format_prompt(user_input)
    response = get_recipe_response(chat, prompt)
    print(f"\nRecipeBot:\n{response}")
