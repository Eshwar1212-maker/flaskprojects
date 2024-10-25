import uuid
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
import os

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
api_key = os.environ["TWILIO_API_KEY_SID"]
api_secret = os.environ["TWILIO_API_KEY_SECRET"]

def get_access_token(room_name):
    # Create the access token
    identity = uuid.uuid4().int
    access_token = AccessToken(account_sid, api_key, api_secret, identity=identity)
    # Create the video grant
    video_grant = VideoGrant(room=room_name)
    # Add the video grant to the access token
    access_token.add_grant(video_grant)
    return access_token.to_jwt()
