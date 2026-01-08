from groq import Groq
import os
import sys

# Optionally load a .env file if python-dotenv is installed.
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # dotenv is optional; continue without it if not installed
    pass

# List of environment variables this script uses / recommends
required_env_vars = [
    "GROQ_API_KEY",      # required: API key for Groq client
    "GROQ_PROJECT_ID",   # optional: project identifier (if applicable)
    "ENV",               # optional: runtime environment (development|production)
]

# Print environment variables status
missing = [v for v in required_env_vars if not os.getenv(v)]
if missing:
    print("Warning: The following recommended environment variables are not set:")
    for v in missing:
        print(f" - {v}")
    print("You should set GROQ_API_KEY at minimum. Example (Linux/macOS):")
    print("  export GROQ_API_KEY='your_api_key_here'")
    print("Or create a .env file with GROQ_API_KEY=your_api_key_here and install python-dotenv to load it automatically.")
    print()

# Load API key from environment; do NOT hard-code secrets in source
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    sys.exit("Error: GROQ_API_KEY is not set. Aborting to avoid exposing secrets or using an invalid key.")

# Create client using the environment-provided key
client = Groq(api_key=api_key)

# Test if key works
try:
    models = client.models.list()
    print("API KEY WORKS! Available models:")
    for m in models.data:
        print(f"- {m.id}")
except Exception as e:
    print("Failed to list models. Check your GROQ_API_KEY and network connectivity.")
    print("Error:", repr(e))
    sys.exit(1)
 
    
    #this code shows the same output, i.e the avaliable list of models using GROQ (that includes llama and many more models)
