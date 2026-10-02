from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "EduGenie is running!"
    })


@app.route("/api/chat", methods=["POST"])
def chat():

    try:
        data = request.get_json()

        question = data.get("question", "").strip()

        if not question:
            return jsonify({
                "answer": "Please enter a question."
            }), 400

        if not GEMINI_API_KEY:
            return jsonify({
                "answer": "Gemini API key is not configured."
            }), 500

        prompt = f"""
You are EduGenie, a friendly AI learning assistant.

Help students understand concepts in a simple and clear way.

Question:
{question}

Give a helpful educational answer.
Use simple English and examples when useful.
"""

        response = model.generate_content(prompt)

        answer = response.text

        return jsonify({
            "answer": answer
        })

    except Exception as e:

        print("Error:", e)

        return jsonify({
            "answer": "Sorry, I couldn't process your question right now."
        }), 500


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
