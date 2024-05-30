from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define a function you want to use in your frontend
def some_python_function(data):
    # For example, just reversing a string
    return data[::-1]

@app.route('/api/process', methods=['POST'])
def process():
    data = request.json
    input_text = data.get('input')
    result = some_python_function(input_text)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
