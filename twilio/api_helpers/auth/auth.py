from flask import Blueprint, request, jsonify
from database.db import create_user, verify_user

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Call create_user from db.py to insert the user into MongoDB
    result = create_user(username, email, password)
    return jsonify({"message": "User registered successfully", "user_id": str(result.inserted_id)}), 201

@auth_blueprint.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    # Verify user credentials using verify_user from db.py
    user = verify_user(email, password)
    if user:
        return jsonify({"message": "Login successful", "user_id": str(user["_id"])}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
