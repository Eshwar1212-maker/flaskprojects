from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from flask_pymongo import PyMongo
import os
from api_helpers.room.room import find_or_create_room
from api_helpers.room.access_token import get_access_token

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Set up MongoDB URI from environment variables
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

# Initialize Flask-PyMongo with the Flask app
mongo = PyMongo(app)

@app.route('/join-room', methods=['POST'])
def create_room_endpoint():
    room_name = request.json.get("room_name")
    find_or_create_room(room_name)
    access_token = get_access_token(room_name)
    return jsonify({"token": access_token})

@app.route('/')
def serve_homepage():
    return "Home page"

if __name__ == '__main__':
    app.run(debug=True)
