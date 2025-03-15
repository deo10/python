# pip3 install openai
# pip3 install python-dotenv

# filepath: /c:/Users/Andrei_Panov/Documents/code/python/open_AI.py
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Set the API key
client = openai.OpenAI(api_key=openai_api_key)

# article

article = "Анчелотти о словах Пепа «вероятность пройти дальше – 1%»: «На самом деле он так не думает, как и мы не думаем, что наши шансы – 99%. У «Реала» есть небольшое преимущество»"

# prompt

prompt = f"Translate the following article: {article}"

# Make the request to OpenAI
def article_translator(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content":prompt},
                  {"role":"assistant", "content":"You are professional translator"}, #adding a role for reply
                  {"role":"system", "content":"Direct English translator"}], #adding style
        max_tokens=100,
        temperature=0,
)
    return response.choices[0].message.content

# Return the receipe
print(article_translator(prompt))