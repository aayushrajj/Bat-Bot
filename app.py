from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai
import sys
import os

app = Flask(__name__)
CORS(app)

# Define a function you want to use in your frontend
def some_python_function(data):
    # For example, just reversing a string
    return data[::-1]

def talk_to_gemini(user_prompt):
    apikey = os.environ.get("GOOGLE_API_KEY")
    if apikey is None:
        raise ValueError("GOOGLE_API_KEY is not set in the environment.")
    genai.configure(api_key=apikey)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_prompt)
    return response.text;

@app.route('/api/process', methods=['POST'])
def process():
    data = request.json
    input_text = data.get('input')
    # result = some_python_function(input_text)
    result = talk_to_gemini(input_text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
