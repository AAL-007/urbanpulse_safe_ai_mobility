import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
# this is GROQ_API_KEY - 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

resp = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "system", "content": "You are an EV fleet planning assistant."},
        {"role": "user", "content": "Plan charging for 3 buses and 1 depot for the next 3 hours."}
    ],
    temperature=0.2,
    max_tokens=10,
)

print(resp.choices[0].message.content)


