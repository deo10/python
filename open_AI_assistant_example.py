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

# assistant code
# kaggle as source for test dataset

# read csv file

df = pd.read_csv("/Users/Andrei_Panov/Downloads/car_price_dataset.csv")

# function reads the file and provides output

def analyze_data(df):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content": f"You are a research assistant. Provide key insights from {df} in point form"}],
        max_tokens=500,
        temperature=0.2,
)
    return response.choices[0].message.content


print(analyze_data(df))