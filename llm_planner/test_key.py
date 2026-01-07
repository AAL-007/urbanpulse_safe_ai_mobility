from groq import Groq

client = Groq(api_key="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")

# Test if key works
models = client.models.list()
print("API KEY WORKS! Available models:")
for m in models.data:
    print(f"- {m.id}")
