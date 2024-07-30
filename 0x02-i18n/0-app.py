#!/usr/bin/env python3
"""
Flask application that renders a "Hello world" message.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """
    Render the index.html template.

    Returns:
        str: The rendered HTML content.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

