from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai
import sys
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

apikey = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=apikey)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Define a function you want to use in your frontend
def some_python_function(data):
    # For example, just reversing a string
    return data[::-1]

def talk_to_gemini(user_prompt):
    apikey = os.getenv('GOOGLE_API_KEY')
    # apikey = os.environ.get("GOOGLE_API_KEY")
    if apikey is None:
        raise ValueError("GOOGLE_API_KEY is not set in the environment.")
    genai.configure(api_key=apikey)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_prompt)
    return response.text

def conversation_with_gemini(user_prompt):
    response = chat.send_message(user_prompt,stream=True)
    answer=""
    for chunk in response:
        answer = chunk.text
    answer2=""
    for message in chat.history:
        answer2 = message.parts[0].text
    return answer2
    

@app.route('/api/process', methods=['POST'])
def process():
    data = request.json
    input_text = data.get('input')
    # result = talk_to_gemini(input_text)
    result = conversation_with_gemini(input_text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
