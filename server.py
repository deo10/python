import os
from flask import Flask, request, render_template_string
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() # Load environment variables from .env file

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
    base_url=os.environ.get('LLM_ENDPOINT')
)

@app.route('/', methods=['GET', 'POST'])
def index():
    poem = None
    if request.method == 'POST':
        try:
            input_message = request.form['input']
            
            response = client.chat.completions.create(
                model=os.environ.get('MODEL'),
                messages=[
                    {'role': 'system', 'content': 'You are a chatbot which specializes in writting poems'},
                    {'role': 'user', 'content': input_message}
                    ]
            )
            
            poem = response.choices[0].message.content
        except Exception as e:
            print("Error:", str(e))
            poem = "An error occurred. Please try again."
            
    return render_template_string(HTML_TEMPLATE, poem=poem)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))
    app.run(host="0.0.0.0", port=port)