import os
from flask import Flask, render_template, request, jsonify
from chatbot import respond

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    bot_response = respond(user_message)

    return jsonify({
        "response": bot_response
    })

if __name__ == "__main__":
      app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
