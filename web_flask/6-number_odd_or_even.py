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
        - ✅/number_template/<n>: display a HTML page only if n is an integer:
            - H1 tag: “Number: n” inside the tag BODY
        - /number_odd_or_even/<n>: display a HTML page only if n is an integer:
            - H1 tag: “Number: n is even|odd” inside the tag BODY
    - ✅You must use the option strict_slashes=False in your route definition
"""
from flask import Flask, render_template
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


@app.route("/python/", defaults={"text" : "is cool"}, strict_slashes=False)
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """number_template"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """number_template"""
    rend_str = f"{n} is even"

    if int(n) % 2 == 0:
        rend_str = f"{n} is even"
    else:
        rend_str = f"{n} is odd"

    return render_template("6-number_odd_or_even.html", rend_str=rend_str)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
