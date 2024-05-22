from flask import Flask, render_template, request, session, redirect, json, url_for, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)