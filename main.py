"""Lab step: generate your first AI response with the OpenAI API."""
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

# Read variables from the .env file into the environment
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    sys.exit("OPENAI_API_KEY not found. Copy .env.example to .env and add your key.")

client = OpenAI(api_key=api_key)
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

response = client.responses.create(
    model=model,
    instructions="You are a friendly tutor who explains things simply.",
    input="Explain what an API is in three sentences.",
)

print(response.output_text)
