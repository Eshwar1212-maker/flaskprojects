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


@app.route('/')
def hello():
    return "Hello Flask"

if __name__ == '__main__':
    app.run(debug=True)


