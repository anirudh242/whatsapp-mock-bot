from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)


def mockify(text):
    new = []
    for i in text:
        rand = random.randint(0, 50)
        if rand % 2 == 0:
            new.append(i.upper())
        else:
            new.append(i.lower())
    return "".join(new)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    print(mockify(incoming_msg))
    msg.body(mockify(incoming_msg))
    return str(resp)


if __name__ == '__main__':
    app.run()
