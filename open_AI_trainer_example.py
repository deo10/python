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

# trainer code

#fitness data

df = pd.read_csv("/Users/Andrei_Panov/Downloads/car_price_dataset.csv")


#add fitness goals into a list
goals = []

while True:
    goal = input("Enter your fitness goals. Type done once complete")
    if goal.lower() == "done":
        break
    
    goals.append(goal)

#pass goals to the model
def trainer(goals, df):
    
    messages = []
    
    for goal in goals:
        messages.append({"role":"user", "content":goal})
        
    messages.extend([
        {"role":"system", "content":"direct, point"},
        {"role":"assistant", "content": f"You are a fitness trainer. The person you are responding to is an accountant. Be specific to their role. Be technical and specific. Reference this data {df} in your response and provide solutions to the {goals}"}]
    )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=10,
        temperature=0,
)
    return response.choices[0].message.content

# Return the receipe
print(trainer(goals, df))