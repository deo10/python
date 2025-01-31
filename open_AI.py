# pip3 install openai
# pip3 install python-dotenv

# filepath: /c:/Users/Andrei_Panov/Documents/code/python/open_AI.py
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Set the API key
client = OpenAI(api_key=openai_api_key)

# Define the question
prompt = "Who is better MJ or LeBron?"

# Make the request to OpenAI
def prompt_engine(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content":prompt}],
        max_tokens=10,
        temperature=0,
)

# Print the request and result
print(prompt_engine(prompt))