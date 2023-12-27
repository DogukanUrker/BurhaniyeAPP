import socket
import secrets
from flask import Flask, render_template
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


@app.route("/tebrikler1")
def greet1():
    return render_template("greet1.html")


@app.route("/tebrikler2")
def greet2():
    return render_template("greet2.html")


@app.route("/tebrikler3")
def greet3():
    return render_template("greet3.html")


@app.route("/tebrikler4")
def greet4():
    return render_template("greet4.html")


@app.route("/tebrikler5")
def greet5():
    return render_template("greet5.html")


@app.route("/zeytin")
def zeytin():
    return render_template("zeytin.html")


@app.route("/halkoyunlari")
def halkoyunlari():
    return render_template("halkoyunlari.html")


@app.route("/elsanatlari")
def elsanatlari():
    return render_template("elsanatlari.html")


@app.route("/deveguresi")
def deveguresi():
    return render_template("deveguresi.html")


@app.route("/necdettosun")
def necdettosun():
    return render_template("necdettosun.html")


@app.route("/erdaltosun")
def erdaltosun():
    return render_template("erdaltosun.html")


@app.route("/turkuler")
def turkuler():
    return render_template("turkuler.html")


@app.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404


@app.route("/soru1")
def q1():
    return render_template("q1.html")


@app.route("/soru2")
def q2():
    return render_template("q2.html")


@app.route("/soru3")
def q3():
    return render_template("q3.html")


@app.route("/soru4")
def q4():
    return render_template("q4.html")


@app.route("/soru5")
def q5():
    return render_template("q5.html")


@app.route("/soru6")
def q6():
    return render_template("q6.html")


@app.route("/soru7")
def q7():
    return render_template("q7.html")


@app.route("/soru8")
def q8():
    return render_template("q8.html")


@app.route("/soru9")
def q9():
    return render_template("q9.html")


@app.route("/soru10")
def q10():
    return render_template("q10.html")


if __name__ == "__main__":
    app.run(
        debug=True,
        host=socket.gethostbyname(socket.gethostname()),
    )
