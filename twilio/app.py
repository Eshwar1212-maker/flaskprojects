from flask import Flask, render_template, request
from dotenv import load_dotenv
from twilio_helpers.room_utils import find_or_create_room
from twilio_helpers.token_utils import get_access_token

load_dotenv()

app = Flask(__name__)

@app.route('/')
def serve_homepage():
    return "Home page"

if __name__ == '__main__':
    app.run(debug=True)
