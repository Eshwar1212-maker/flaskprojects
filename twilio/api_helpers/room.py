
import twilio.rest

import os
from dotenv import load_dotenv
load_dotenv()

#Create a twilio client
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
api_key = os.environ["TWILIO_API_KEY_SID"]
api_secret = os.environ["TWILIO_API_KEY_SECRET"]
twilio_client = twilio.rest.Client(api_key, api_secret, account_sid)

def find_or_create_room(room_name):
    try:
        # Try to fetch an in-progress room with this name
        twilio_client.video.rooms(room_name).fetch()
    except:
        # The room did not exist, so create it
        twilio_client.video.rooms.create(unique_name=room_name, type="go")