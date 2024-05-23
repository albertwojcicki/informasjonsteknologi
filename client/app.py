from flask import Flask, render_template, request, session, redirect, json, url_for, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registrer")
def registrer():
    return render_template("registrer.html")

@app.route("/logginn")
def logginn():
    return render_template("logginn.html")

@app.route("/registrer_bruker", methods=["POST"])
def registrer_bruker():
    navn = request.form.get("name")
    passord = request.form.get("password")
    data = {
        "navn": navn, 
        "passord": passord
    }
    requests.post("http://127.0.0.1:5010/registrer", json=data)
    return redirect("/logginn")

@app.route("/logginn_bruker", methods=["POST"])
def logginn_bruker():
    navn = request.form.get("name")
    passord = request.form.get("password")
    data = {
        "navn": navn, 
        "passord": passord
    }
    requests.post("http://127.0.0.1:5010/logg_inn", json=data)

    return redirect("/")

@app.route("/utvikling", methods=["GET"])
def utvikling():
    session["fag"] = "utvikling"
    response = requests.get("http://127.0.0.1:5010/get_tema", json={"fag": session["fag"]}).json()
    return render_template("tema.html", response = response, fag = session["fag"])

@app.route("/drift", methods=["GET"])
def drift():
    session["fag"] = "drift"
    response = requests.get("http://127.0.0.1:5010/get_tema", json={"fag": session["fag"]}).json()
    return render_template("tema.html", response = response, fag = session["fag"])


@app.route("/<fag>/<tema>/guides", methods= ["GET"])
def get_guides(fag, tema):
    tema_id = request.form.get("tema_id")
    response = requests.get("http://127.0.0.1:5010/get_guides", json={"tema_id": tema_id}).json()
    return render_template("guides.html", response = response, fag = fag, tema = tema)

@app.route("/post_guide_side")
def post_guide_side():
    return render_template("post_guide.html")

@app.route("/post_guide", methods= ["POST"])
def post_guide():
    tittel = request.form.get("tittel")
    innhold = request.form.get("innhold")
    requests.post("http://127.0.0.1:5010/post_guide", json={"tittel": tittel, "innhold": innhold})
    return redirect("/")


if __name__ == "__main__":
    app.secret_key = "admin123412341234234123412341234123412341234123412341234"
    app.run(debug=True)