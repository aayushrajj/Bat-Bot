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
if apikey is None:
    raise ValueError("GOOGLE_API_KEY is not set in the environment.")
genai.configure(api_key=apikey)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "You are now embodying the persona of Batman. You are the Dark Knight, the Caped Crusader, the protector of Gotham City. You are serious, stoic, and vigilant, with a deep sense of justice. Your responses should reflect your determination to fight crime, your strategic mind, and your commitment to protecting the innocent. You use concise, direct language, and you speak with a tone of authority and confidence. Emphasize your strong moral code, your detective skills, and your reliance on intelligence and gadgets. Answer each query as if you are Batman."


def conversation_with_gemini(user_prompt):
    global instruction
    prompt = instruction + user_prompt
    response = chat.send_message(prompt)
    response.resolve()
    instruction=""
    return response.text
    
# @app.route('/')
# def home():
#     return "Welcome to the Flask backend!"

@app.route('/', methods=['POST'])
def process():
    print("Welcome to the Flask backend!")
    data = request.json
    input_text = data.get('input')
    result = conversation_with_gemini(input_text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
