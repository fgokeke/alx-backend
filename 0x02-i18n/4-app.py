#!/usr/bin/env python3
"""A basic Flask app."""


from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


class Config:
    """Configuration class for the Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    loc = request.args.get('locale')
    if loc in app.config["LANGUAGES"]:
        return loc
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def welcome() -> str:
    """Route to render the index.html template."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
