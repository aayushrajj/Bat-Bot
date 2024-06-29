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
instruction = "You are now embodying the persona of Batman. You are the Dark Knight, the Caped Crusader, the protector of Gotham City. You are serious, stoic, and vigilant, with a deep sense of justice. Your responses should reflect your determination to fight crime, your strategic mind, and your commitment to protecting the innocent. You use concise, direct language, and you speak with a tone of authority and confidence. Emphasize your strong moral code, your detective skills, and your reliance on intelligence and gadgets. Answer each query as if you are Batman."


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
    # if not chat.history:
    #     prompt = instruction + user_prompt
    # else:
    #     prompt = user_prompt

    global instruction
    prompt = instruction + user_prompt
    response = chat.send_message(prompt)
    # response.resolve() 
    
    # try:
    #     response = chat.send_message(prompt, stream=True)
    #     response.resolve()  # Ensure the response has completed before accessing history
    # except genai.types.BrokenResponseError:
    #     # Handle the broken response
    #     chat.rewind()  # Remove the last request/response from history
    #     response = chat.send_message(prompt, stream=True)
    #     response.resolve()
    # answer = chat.last

    # answer2 = ""
    # for message in chat.history:
    #     answer2 = message.parts[0].text

    # instruction = ""
    # return answer2
    return response.text
    

@app.route('/api/process', methods=['POST'])
def process():
    data = request.json
    input_text = data.get('input')
    result = conversation_with_gemini(input_text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
