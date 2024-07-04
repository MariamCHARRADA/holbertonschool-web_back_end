#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route("/")
def index():
    """renders template"""
    return render_template("0-index.html")


class Config:
    """ config module"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
