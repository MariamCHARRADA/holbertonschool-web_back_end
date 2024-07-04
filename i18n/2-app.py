#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel
from os import getenv

app = Flask(__name__)
babel = Babel(app, static_url_path='')


class Config(object):
    """ config module"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@babel.localeselector
def get_locale() -> str:
    """ determines the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """renders template"""
    return render_template("2-index.html")


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
