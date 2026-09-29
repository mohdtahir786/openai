"""Bonus: a small terminal chatbot that remembers the conversation."""
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    sys.exit("OPENAI_API_KEY not found. Copy .env.example to .env and add your key.")

client = OpenAI(api_key=api_key)
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# The API is stateless: we resend the whole history on every turn.
history = []

print(f"Chatting with {model}. Type 'quit' to exit.\n")

while True:
    user_text = input("You: ").strip()
    if user_text.lower() in {"quit", "exit"}:
        break
    if not user_text:
        continue

    history.append({"role": "user", "content": user_text})

    try:
        response = client.responses.create(
            model=model,
            instructions="You are a helpful, concise assistant.",
            input=history,
        )
    except OpenAIError as e:
        print(f"[API error] {e}\n")
        history.pop()  # drop the failed message so history stays consistent
        continue

    reply = response.output_text
    history.append({"role": "assistant", "content": reply})
    print(f"AI: {reply}\n")
