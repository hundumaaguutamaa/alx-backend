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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """Return a user dictionary or None if the ID cannot be found or login_as was not passed."""
    login_as = request.args.get('login_as')
    if login_as:
        user_id = int(login_as)
        return users.get(user_id)
    return None

@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    
    user = g.get('user')
    if user and user['locale'] in Config.LANGUAGES:
        return user['locale']
    
    return request.accept_languages.best_match(Config.LANGUAGES)

@app.before_request
def before_request():
    """Before request handler to set language globally."""
    user = get_user()
    g.user = user
    g.lang = get_locale()

@app.route('/')
def get_index() -> str:
    """The home/index page."""
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

