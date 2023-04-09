#!/usr/bin/env

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
	return jsonify({"message": "Welcome to the API. Get an API key from uhaiweb.afrika/api"})


@app.route('/auth', methods=['GET'])
def auth():
    return jsonify({
        "message": "Auth route",
        "routes": [
            "/startSession",
            "/endSession",
            "/sendQuery",
            "/receiveQuery",
            "/chat/send",
            "/chat/receive"
        ]
    })

@app.route('/chat/send', methods=['POST'])
def sendMsg():
    message = request.form.chatMessage
    return jsonify({"message": "Send message"})

@app.route('/chat/receive', methods=['POST'])
def pollMsgs():
    return jsonify({"message": "Polling any new messages"})

@app.route('/sendQuery', methods=['GET'])
def sendChatbot():
    return jsonify({"message": "Send query to chatbot"})

@app.route('/endSession', methods=['GET'])
def endSession():
    return jsonify({"message": "End current chat session"})

@app.route('/startSession', methods=['GET'])
def startSession():
    return jsonify({"message": "Start session"})



if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
