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

# create new empty list
ingrediens = []

# enter user ingrediens and populate the list
while True:
    ingredient = input("Enter your ingrediens. Type done once complete")
    if ingredient.lower() == "done":
        break
    
    ingrediens.append(ingredient)

# Make the request to OpenAI - pay attention on output format
def receipe_gen(ingrediens):
    
    messages = []
    
    for ingredient in ingrediens:
        messages.append({"role":"user", "content":ingredient})
        
    messages.extend([
        {"role":"system", "content":"JSON format"}, #example of structured output
        {"role":"assistant", "content":"You are a high-end chef. Generate a recipe based on given ingredients. Must be in JSON format"}]
    )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=10,
        temperature=0,
)
    return response.choices[0].message.content

# Return the receipe
print(receipe_gen(ingrediens))