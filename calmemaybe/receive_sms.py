from flask import Flask, request, redirect
from flask_ngrok import run_with_ngrok
from twilio.twiml.messaging_response import MessagingResponse
import threading
import os
from os import environ
from flask_sqlalchemy import SQLAlchemy


import sys
from twilio.rest import Client
from send_sms import send_emergency_message, send_informational_message

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a MMS message."""
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    #check if message starts with "hi"
    if body == 'calmemaybe':
        resp.message("hi! are you leaving your current location (Y/N)")
    
    #check if message is Y
    elif body == 'Y':
        resp.message("awesome! when do you expect to reach? tell us how many minutes (ex: 16)")

    # #to check is string is a number in string form with a null check
    elif body and body.isnumeric():
        resp.message("great! we'll let your contacts know - bon voyage :). If you want to log a delay at any point, type D")
        send_informational_message("+16504417802", "dhruti", int(body))
        t = threading.Timer(int(body)*60.0, lambda : send_emergency_message("+16504417802", "dhruti"))
        t.start()
    
    elif body and "arrive" in body:
        resp.message("thanks for using calmemaybe, glad you're safe :)")

    return str(resp)


if __name__ == "__main__":
    app.run()