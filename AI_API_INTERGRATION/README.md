# AI API Integration Assignment

## Project Description
This project demonstrates integration with multiple Generative AI APIs using Python.  
Each program sends a user prompt to a different AI provider and displays the generated response.

The APIs used in this project are:
- Groq
- Ollama
- Hugging Face
- Cohere
- Google Gemini

---

## Setup Instructions

1. Clone the repository or download the files.

2. Install required Python libraries:

pip install -r requirements.txt

3. Set environment variables for API keys.

For Windows PowerShell:

$env:GROQ_API_KEY="your_key_here"
$env:HUGGINGFACE_API_KEY="your_key_here"
$env:COHERE_API_KEY="your_key_here"
$env:GOOGLE_API_KEY="your_key_here"

4. Install and run Ollama from:

https://ollama.ai/

Then start a model:

ollama run llama2

---

## How to Obtain API Keys

### Groq
1. Go to https://console.groq.com
2. Create an account
3. Generate an API key from the dashboard

### Hugging Face
1. Go to https://huggingface.co
2. Open Settings → Access Tokens
3. Create a new token

### Cohere
1. Go to https://dashboard.cohere.com
2. Sign up
3. Generate an API key

### Ollama
Download and install from https://ollama.ai  
No API key required.

###Gemini
Go to Google AI Studio.

Click on the "Get API key" button in the left sidebar.

Click "Create API key in new project".

Copy the generated key.
---

## How to Run Each Program

Groq:

python groq_example.py

Ollama:

python ollama_example.py

Hugging Face:

python huggingface_example.py

Cohere:

python cohere_example.py

Google Gemini:

python gemini_example.py

Each program will ask for a prompt and return an AI-generated response.

---

## Screenshots

Screenshots of the program outputs are included in the **screenshots** folder.