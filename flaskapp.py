from flask import Flask, jsonify, request
from cliftonai.chatbot import Chatbot

app = Flask(__name__)
chatbot = Chatbot()

@app.route('/ask/', methods=['POST'])
def ask():
    request_json = request.get_json()
    chatbot_response = chatbot.ask(request_json['question'])
    return jsonify(chatbot_response._asdict())
