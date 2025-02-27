#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome():
    """Return a welcome message"""
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def users():
    """Return a list of users"""
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(400, description="Missing email or password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"})
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
