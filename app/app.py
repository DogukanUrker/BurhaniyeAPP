import socket
import secrets
from flask import Flask, render_template, redirect
from data.foods import foodName, foodImage, foodSound
from data.locations import locationName, locationImage, locationSound
from data.places import placeName, placeImage, placeSound

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tarihce")
def history():
    return render_template("history.html")


@app.route("/yemekler/<id>")
def yemekler(id):
    id = int(id)
    return render_template(
        "foods.html",
        id=id,
        foodName=foodName[id],
        foodImage=foodImage[id],
        foodSound=foodSound[id],
    )


@app.route("/yerler/<id>")
def locations(id):
    id = int(id)
    return render_template(
        "locations.html",
        id=id,
        locationName=locationName[id],
        locationImage=locationImage[id],
        locationSound=locationSound[id],
    )


@app.route("/mekanlar/<id>")
def places(id):
    id = int(id)
    return render_template(
        "places.html",
        id=id,
        placeName=placeName[id],
        placeImage=placeImage[id],
        placeSound=placeSound[id],
    )


@app.route("/hakkinda")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(
        debug=True,
        host=socket.gethostbyname(socket.gethostname()),
    )
