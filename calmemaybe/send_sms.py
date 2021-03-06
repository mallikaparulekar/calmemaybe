# Download the helper library from https://www.twilio.com/docs/python/install
import os
from os import environ
import sys
from twilio.rest import Client
# from dotenv import load_dotenv

# load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def send_informational_message(receiving_phone_num_str, person_name, time ):
    # account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    # auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    account_sid = 'xxxxxxxxxx'
    auth_token = 'xxxxxxxxxx'
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="your friend {0} has started a trip. they plan to reach in {1} minutes. just thought you should know :) ".format(person_name, time),
                        from_='+14703478946',
                        to=receiving_phone_num_str
                    )
    print(message.sid)

def send_emergency_message(receiving_phone_num_str, person_name):
    account_sid = 'xxxxxxxxxx'
    auth_token = 'xxxxxxxxxx'
    print(account_sid, auth_token)
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="your friend {} has not indicated that they have reached their destination on time. danger!!! ".format(person_name),
                        from_='+14703478946',
                        to=receiving_phone_num_str
                    )
    print(message.sid)


