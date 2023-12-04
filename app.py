import json
import socket
import secrets
from random import choice
from flask import Flask, render_template, redirect


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tarihce")
def history():
    return render_template("history.html")


@app.route("/yiyecekler")
def yiyecekler():
    file = open("foods.json")
    data = json.load(file)
    food = data[0]

    return render_template(
        "foods.html",
        foodID=food["id"],
        foodName=food["name"],
        foodImage=food["image"],
        foodSound=food["sound"],
    )


@app.route("/yerler")
def locations():
    return render_template("locations.html")


@app.route("/mekanlar")
def places():
    return render_template("places.html")


@app.route("/hakkinda")
def about():
    return render_template("about.html")


@app.errorhandler(404)
def notFound(e):
    return redirect("/"), 301


if __name__ == "__main__":
    app.run(
        debug=True,
        host=socket.gethostbyname(socket.gethostname()),
    )
