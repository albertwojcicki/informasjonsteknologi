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
    return render_template("index.html")

@app.route("/logginn_bruker", methods=["POST"])
def logginn_bruker():
    name = request.form.get("name")
    password = request.form.get("password")

if __name__ == "__main__":
    app.run(debug=True)