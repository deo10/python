# pip3 install openai
# pip3 install python-dotenv
# pip3 install pandas

# filepath: /c:/Users/Andrei_Panov/Documents/code/python/open_AI.py
from openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Set the API key
client = OpenAI(api_key=openai_api_key)

# Batch processing example

prompts = ["Tell me a story about a warrior princess",
           "Generate a list of 5 business ideas",
           "Write a poem about Michael Jordan"]

def process_promts(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        max_tokens=10,
        temperature=0,
)
    return response.choices[0].message.content

results = []

for prompt in prompts:
    result = process_promts(prompt)
    results.append(result)
    
for i in enumerate(results):
    print(f"Prompt {i+1}: {prompt}")
    print(f"Response {i+1}: {result}\n")
    