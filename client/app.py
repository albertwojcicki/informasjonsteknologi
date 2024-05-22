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

@app.route("/registrer_bruker", metohds=["POST"])
def registrer_bruker():
    name = request.form.get("name")
    password = request.form.get("password")
    data = {
        "name": name, 
        "password": password
    }
    requests("http://127.0.0.1:5010")

@app.route("/logginn_bruker", metohds=["POST"])
def logginn_bruker():
    name = request.form.get("name")
    password = request.form.get("password")

if __name__ == "__main__":
    app.run(debug=True)