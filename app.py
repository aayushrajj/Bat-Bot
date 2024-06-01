from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_google_genai import GoogleGenerativeAI
import sys

app = Flask(__name__)
CORS(app)

# set 
os.environ['GOOGLE_API_KEY'] = str("AIzaSyACpTe1Ein41EI9Oo4y-0VrwkrL8l7_MEY")

# Define a function you want to use in your frontend
def some_python_function(data):
    # For example, just reversing a string
    return data[::-1]

def talk_to_gemini(user_prompt):
    return ;ß

@app.route('/api/process', methods=['POST'])
def process():
    data = request.json
    input_text = data.get('input')
    result = some_python_function(input_text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
