from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/whatsapp", methods=['GET', 'POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'hi' in incoming_msg:
        msg.body("Hello! How can I help you today?")
        responded = True
    if 'bye' in incoming_msg:
        msg.body("Goodbye! Have a great day ahead.")
        responded = True
    if not responded:
        msg.body("I'm sorry, I didn't understand that. Could you please try again?")
    return str(resp)

if __name__ == "__main__":
    app.run()
