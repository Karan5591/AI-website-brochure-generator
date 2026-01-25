import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key or len(api_key) < 10:
    raise ValueError("OPENAI_API_KEY not found")

MODEL = "gpt-5-nano"
openai = OpenAI()
