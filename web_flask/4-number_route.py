#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
    - ✅Your web application must be listening on 0.0.0.0, port 5000
    - Routes:
        - ✅/: display “Hello HBNB!”
        - ✅/hbnb: display “HBNB”
        - ✅/c/<text>: display “C ” followed by the value of the text variable
          (replace underscore _ symbols with a space )
        - ✅/python/<text>: display “Python ”, followed by the value of the text
          variable (replace underscore _ symbols with a space )
            - The default value of text is “is cool”
        - ✅/number/<n>: display “n is a number” only if n is an integer
    - ✅You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """c/route!"""
    text = escape(text).split("_")
    text = " ".join(text)
    return f"C {text}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """python_route"""
    text = escape(text).split("_")
    text = " ".join(text)
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """number_route"""

    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
