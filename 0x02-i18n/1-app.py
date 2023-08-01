from flask import Flask, render_template, request, redirect, url_for, flash
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

if __name__ == '__main__':
    app.run(debug=True)