import jwt
import datetime
from flask import request, jsonify

SECRET_KEY = "mysecret"  # Same as in security.py

# Hardcoded user credentials for demo purposes
USERS = {
    "admin": {"password": "admin", "scope": "read write delete"},
    "viewer": {"password": "viewer", "scope": "read"}
}

def login():
    """
    Handle user login.
    Generate a JWT token with scopes if credentials are correct.
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Validate credentials
    if username not in USERS or USERS[username]["password"] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    # Create JWT payload
    payload = {
        "sub": username,
        "scope": USERS[username]["scope"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # 1 hour expiry
    }

    # Encode JWT token
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return jsonify({"access_token": token})
