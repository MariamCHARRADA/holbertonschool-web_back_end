#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from os import getenv
from typing import Union

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """config module"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("4-app.Config")


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """renders template"""
    return render_template("5-index.html")


@babel.localeselector
def get_locale() -> str:
    """determines the best lang match"""
    if request.args.get("locale"):
        locale = request.args.get("locale")
        if locale in app.config["LANGUAGES"]:
            return locale
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Union[dict, None]:
    """get user from login_as"""
    if request.args.get("login_as"):
        user = int(request.args.get("login_as"))
        if user in users:
            return users.get(user)
    return None


@app.before_request
def before_request():
    """before_request"""
    g.user = get_user()


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
