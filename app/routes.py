from flask import request, jsonify
from app import app, users_collection

@app.route('/')
def home():
    return jsonify({"message": "Server is running!"})

@app.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user with their preferences.
    """
    data = request.json
    email = data.get("email")
    preferences = data.get("preferences", [])

    if not email:
        return jsonify({"error": "Email is required"}), 400

    # Store user preferences in MongoDB
    users_collection.update_one(
        {"email": email},
        {"$set": {"preferences": preferences}},
        upsert=True
    )

    return jsonify({"message": "User registered successfully"}), 201
