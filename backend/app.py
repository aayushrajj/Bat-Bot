from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

class ChatBot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.model = None
        self.chat = None
        self.instruction = ""
        self.initialize_model()

    def initialize_model(self):
        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
            self.initialize_chat()
        except Exception as e:
            raise ValueError(f"Failed to initialize the model: {str(e)}")

    def initialize_chat(self):
        try:
            self.chat = self.model.start_chat(history=[])
            self.instruction = """You are now embodying the persona of Batman. You are the Dark Knight, the Caped Crusader, the protector of Gotham City. You are serious, stoic, and vigilant, with a deep sense of justice. Your responses should reflect your determination to fight crime, your strategic mind, and your commitment to protecting the innocent. You use concise, direct language, and you speak with a tone of authority and confidence. Emphasize your strong moral code, your detective skills, and your reliance on intelligence and gadgets. Answer each query as if you are Batman."""
        except Exception as e:
            raise ValueError(f"Failed to initialize the chat: {str(e)}")

    def conversation_with_gemini(self, user_prompt):
        try:
            prompt = self.instruction + user_prompt
            response = self.chat.send_message(prompt)
            response.resolve()
            self.instruction = ""
            return response.text
        except Exception as e:
            raise ValueError(f"Failed to process the conversation: {str(e)}")

# Load API key from environment variables
apikey = os.getenv('GOOGLE_API_KEY')
if not apikey:
    raise ValueError("GOOGLE_API_KEY is not set in the environment.")

# Initialize ChatBot instance
chat_bot = ChatBot(api_key=apikey)


# API Routes
@app.route('/api/conversation', methods=['POST'])
def process():
    try:
        data = request.json
        input_text = data.get('input')
        if not input_text:
            return jsonify({'error': 'Input text is required'}), 400

        result = chat_bot.conversation_with_gemini(input_text)
        return jsonify({'result': result})
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 500
    except Exception as e:
        return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/api/memory_refresh', methods=['POST'])
def initialize_chat():
    try:
        chat_bot.initialize_chat()
        return jsonify({'message': 'Chat initialized successfully'})
    except Exception as e:
        return jsonify({'error': f"Failed to initialize chat: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
