from flask import Flask
import os
import uuid
import twilio.jwt.access_token
import twilio.jwt.access_token.grants
import twilio.rest
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

#Create a twilio client
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
api_key = os.environ["TWILIO_API_KEY_SID"]
api_secret = os.environ["TWILIO_API_KEY_SECRET"]
twilio_client = twilio.rest.Client(api_key, api_secret, account_sid)

app = Flask(__name__)

@app.route('/')
def serve_homepage():
    return "Home page"

if __name__ == '__main__':
    app.run(debug=True)

#Request to 
def find_or_create_room(room_name):
    try:
        #try to fetch an in-progress room with this name
        twilio_client.video.rooms(room_name).fetch()
    except:
        #the room did not exist, so create it
        twilio_client.video.rooms.create(unique_name=room_name, type="go")

        

