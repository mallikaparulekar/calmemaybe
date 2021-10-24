from flask import Flask, request, redirect
from flask_ngrok import run_with_ngrok
from twilio.twiml.messaging_response import MessagingResponse
import threading
import os

# Download the helper library from https://www.twilio.com/docs/python/install
import os
import sys
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def send_informational_message(receiving_phone_num_str, person_name, time ):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="your friend {0} has started a trip. they plan to reach in {1} minutes. just thought you should know :) ".format(person_name, time),
                        from_='+14703478946',
                        to=receiving_phone_num_str
                    )
    print(message.sid)

def send_emergency_message(receiving_phone_num_str, person_name):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="your friend {} has not indicated that they have reached their destination on time. danger!!! ".format(person_name),
                        from_='+14703478946',
                        to=receiving_phone_num_str
                    )
    print(message.sid)

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
        send_emergency_message("+16504417802", "kalie")
        send_informational_message("+18585681775", "kalie", str(body))

    elif body and "arrive" in body:
        resp.message("thanks for using calmemaybe, glad you're safe :)")

# # Add a text message
# msg = resp.message("The Robots are coming! Head for the hills!")

# # Add a picture message
# msg.media(
#     "https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg"
# )

    return str(resp)


if __name__ == "__main__":
    app.run()