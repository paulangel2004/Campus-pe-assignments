import os
from google.genai import Client

api_key = os.getenv("GOOGLE_API_KEY")
client = Client(api_key=api_key)

def query_api(prompt):
    """Query the Google Gemini API with a prompt"""
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Google Gemini API...")
    result = query_api(user_prompt)
    print("\nResponse:")
    print(result)