from flask import Flask, request, redirect
from flask_ngrok import run_with_ngrok
from twilio.twiml.messaging_response import MessagingResponse

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
    #app.run(debug=True)
    app.run()



# from flask import Flask
# from flask_ngrok import run_with_ngrok
  
# app = Flask(__name__)
# run_with_ngrok(app)
  
# @app.route("/")
# def hello():
#     return "Hello Geeks!! from Google Colab"
  
# if __name__ == "__main__":
#   app.run()