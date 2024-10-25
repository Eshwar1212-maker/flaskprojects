from flask import Flask, render_template, request
from dotenv import load_dotenv
from api_helpers.room import find_or_create_room
from api_helpers.access_token import get_access_token

load_dotenv()

app = Flask(__name__)

@app.route('/create_room/<room_name>', methods=['POST'])
def create_room_endpoint(room_name):
    find_or_create_room(room_name)
    return f"Room {room_name} created or fetched", 200

@app.route('/get_token/<room_name>', methods=['GET'])
def get_token_endpoint(room_name):
    token = get_access_token(room_name)
    return token, 200

@app.route('/')
def serve_homepage():
    return "Home page"

if __name__ == '__main__':
    app.run(debug=True)

