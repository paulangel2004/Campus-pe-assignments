import requests

def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama2",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print(query_ollama(user_prompt))