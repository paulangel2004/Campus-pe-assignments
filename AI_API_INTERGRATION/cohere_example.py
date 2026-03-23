import os
import cohere

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.chat(
            model="command-a-03-2025",
            message=prompt,
            max_tokens=100
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print(query_cohere(user_prompt))