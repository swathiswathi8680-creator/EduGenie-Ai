import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Fetch the API key from Render Environment Variables
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({'response': 'Please enter a valid question.'}), 400

        # Using the supported model name
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(user_message)

        return jsonify({'response': response.text})

    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({'response': "Sorry, I couldn't process your question right now."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
