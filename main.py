import random

import pandas as pd
from flask import Flask, render_template, request

APP = Flask(__name__)


@APP.route('/')
def home():
    random_value = random.randint(1, 20)
    return render_template("home.html", random_value=random_value)


@APP.route("/about")
def about():
    table = pd.read_csv("data.csv", index_col="id").to_html(index=False)
    return render_template("about.html", table=table)


@APP.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        df = pd.read_csv("data.csv", index_col="id")
        df.loc[len(df.index)] = [
            request.values.get("Name"),
            request.values.get("Email"),
            request.values.get("Favorite"),
            request.values.get("Message") or " ",
            request.values.get("Surf", False),
            request.values.get("Permission", False),
        ]
        df.to_csv("data.csv")
    return render_template("contact.html")


if __name__ == '__main__':
    APP.run()
