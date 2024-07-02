#!/usr/bin/env python3
"""session authentication views"""

from api.v1.views import app_views
from flask import request, jsonify
from models.user import User
from os import getenv


@app_views.route("api/v1/views/session_auth.py",
                 methods=[POST], strict_slashes=False)
def login():
    """returns logged user"""
    from api.v1.app import auth

    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    userr = user[0]
    if not userr.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(userr.id)
    SESSION_NAME = getenv("SESSION_NAME")
    response = jsonify(userr.to_json())

    response.set_cookie(SESSION_NAME, session_id)

    return response
