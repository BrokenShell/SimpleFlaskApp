from flask import Flask, render_template

APP = Flask(__name__)


@APP.route('/')
def home():
    return render_template("home.html", disabled=True)


@APP.route("/about")
def about():
    return render_template("about.html", disabled=True)


@APP.route("/contact")
def contact():
    return render_template("contact.html", disabled=True)


if __name__ == '__main__':
    APP.run(debug=True)
