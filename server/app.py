from flask import Flask, request
import sqlite3
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

con = sqlite3.connect("database.db", check_same_thread=False)
cur = con.cursor()


@app.route('/registrer', methods=["POST"])
def registrer():
  return 200

@app.route('/logg_inn', methods=["GET"])
def logg_inn():
  return 200
  
@app.route('/get_tema', methods=["GET"])
def get_tema():
  return 200

@app.rotue('/post_tema', methods=["POST"])
def post_tema():
  return 200

@app.route('/get_guides', methods=["POST"])
def get_guides():
  return 200

@app.route('/get_guide', methods=["GET"])
def get_guide():
  return 200

@app.route('/post_guide', methods=["POST"])
def post_guides():
  return 200

@app.route('/get_kommentarer', methods=["POST"])
def get_kommentarer():
  return 200

@app.route('/post_kommentarer', methods=["POST"])
def post_kommentarer():
  return 200
