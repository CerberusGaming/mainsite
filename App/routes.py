from flask import render_template
from flask_nav.elements import Navbar, View, Subgroup, Link
from .flask import app, nav


@nav.navigation()
def mainnavbar():
    return Navbar(
        "Cerberus Gaming",
        View('Home', 'index'),
        View('Test', 'test'),
        Subgroup("Drop",
                 Link("One", "#"),
                 Link("Two", "#")
                 )
    )


@app.route("/")
def index():
    return render_template("pages/index.html")


@app.route("/test")
def test():
    return render_template("pages/test.html")
