from producer import produce
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def root():
    return """
        invoke /send to send messages
    """


@app.route("/send/")
@app.route("/send/<int:count>")
def send_message(count=1):
    message = request.args.get("message")
    produce(message, count=count)
    return message + " Sent"

