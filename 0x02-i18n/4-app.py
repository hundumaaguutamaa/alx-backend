#!/usr/bin/env python3
"""A Basic Flask app."""
from flask_babel import Babel, gettext as _
from flask import Flask, render_template, request, g

class Config:
    """Represents a Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)

@app.before_request
def before_request():
    """Before request handler to set language globally."""
    g.lang = get_locale()

@app.route('/')
def get_index() -> str:
    """The home/index page."""
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

