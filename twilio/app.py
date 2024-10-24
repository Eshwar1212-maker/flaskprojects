from flask import Flask
import os
import uuid
import twilio.jwt.access_token
import twilio.jwt.access_token.grants
import twilio.rest
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

account_sid = os.environ()

#Create a twilio client
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
api_key = os.environ["TWILIO_API_SID"]
api_secret = os.environ["TWILIO_API_KEY_SECRET"]
twilio_client = twilio.rest.Client(api_key, api_secret, account_sid)


@app.route('/')
def hello():
    return "Hello Flask"

if __name__ == '__main__':
    app.run(debug=True)


