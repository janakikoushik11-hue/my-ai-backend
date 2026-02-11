from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key=os.environ.get("API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]
    response = model.generate_content(user_input)
    return jsonify({"reply": response.text})

@app.route("/")
def home():
    return "AI Backend Running"


# IMPORTANT PART
port = int(os.environ.get("PORT", 8080))
app.run(host="0.0.0.0", port=port)
