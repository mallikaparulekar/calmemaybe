# Download the helper library from https://www.twilio.com/docs/python/install
import os
import sys
sys.path.append("/Users/mallikaparulekar/opt/anaconda3/lib/python3.8/site-packages/")
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['AC9812c4a0456958d25531f382f6320f81']
# auth_token = os.environ['83ddb455f7e1c47d5591ab4ae1c0e848']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="we're basically amazing.",
                     from_='+14703478946',
                     to='+16504417802'
                 )

print(message.sid)