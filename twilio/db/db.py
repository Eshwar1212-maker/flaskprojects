from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Set up MongoDB connection
client = MongoClient(os.getenv("MONGODB_URI"))
db = client['your_database_name']

# --- User CRUD Functions ---

def create_user(username, email, password):
    """Insert a new user document with hashed password into the 'users' collection."""
    password_hash = generate_password_hash(password)
    user_data = {
        "username": username,
        "email": email,
        "password_hash": password_hash
    }
    return db.users.insert_one(user_data)

def find_user_by_email(email):
    """Find a user document by email in the 'users' collection."""
    return db.users.find_one({"email": email})

def verify_user(email, password):
    """Verify user credentials."""
    user = find_user_by_email(email)
    if user and check_password_hash(user["password_hash"], password):
        return user  # Authenticated successfully
    return None  # Authentication failed
