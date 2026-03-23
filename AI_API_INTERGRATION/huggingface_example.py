import os
from huggingface_hub import InferenceClient

api_key = os.getenv("HUGGINGFACE_API_KEY")
client = InferenceClient(api_key=api_key)

def query_api(prompt):
    try:
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print(query_api(user_prompt))