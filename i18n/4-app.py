#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
from os import getenv

app = Flask(__name__)
babel = Babel(app)

LANGUAGES = ["en", "fr"]

class Config(object):
    """config module"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("4-app.Config")


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """renders template"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> str:
    """determines the best lang match """
    if request.args.get("locale"):
        locale = request.args.get("locale")
        if locale in LANGUAGES:
            return locale
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
