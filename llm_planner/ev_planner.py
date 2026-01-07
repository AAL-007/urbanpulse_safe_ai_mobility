import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

response = requests.post(OLLAMA_URL, json={
    "model": "gpt4all-gpt2.7b-online",  # YOUR ACTUAL MODEL [file:129]
    "prompt": "test",
    "stream": False
})

print("FULL RAW RESPONSE:")
print(response.json())
