from flask import Flask, request, Response
import sqlite3
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

con = sqlite3.connect("database.db", check_same_thread=False)
cur = con.cursor()


@app.route('/registrer', methods=["POST"])
def registrer():
  navn = request.get_json()["navn"]
  passord = request.get_json()["passord"]

  cur.execute("INSERT INTO brukere(navn, passord) VALUES(?, ?)", (navn, passord))
  return Response(status=200)

@app.route('/logg_inn', methods=["GET"])
def logg_inn():
  return Response(status=200)
  
@app.route('/get_tema', methods=["GET"])
def get_tema():
  return Response(status=200)

@app.route('/post_tema', methods=["POST"])
def post_tema():
  return Response(status=200)

@app.route('/get_guides', methods=["POST"])
def get_guides():
  return Response(status=200)

@app.route('/get_guide', methods=["GET"])
def get_guide():
  return Response(status=200)

@app.route('/post_guide', methods=["POST"])
def post_guides():
  return Response(status=200)

@app.route('/get_kommentarer', methods=["POST"])
def get_kommentarer():
  return Response(status=200)

@app.route('/post_kommentarer', methods=["POST"])
def post_kommentarer():
  return Response(status=200)

if __name__ == "__main__":
  app.run(debug=True, port=5010)