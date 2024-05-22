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
  try:
    navn = request.get_json()["navn"]
    passord = request.get_json()["passord"]

    cur.execute("INSERT INTO brukere(navn, passord) VALUES(?, ?)", (navn, passord))
    con.commit()

    return {"melding": "Bruker ble lagt til"}, 200
  except sqlite3.Error as e:
    return {"error": str(e)}, 500

@app.route('/logg_inn', methods=["POST"])
def logg_inn():
  try:
    navn = request.get_json()["navn"]
    passord = request.get_json()["passord"]
    cur.execute("SELECT id FROM brukere WHERE navn = ? AND passord = ?", (navn, passord))
    id = cur.fetchone()

    if not id:
      return {"error": "Fant ikke bruker"}, 404
    
    return {"id": id[0]}, 200
  except sqlite3.Error as e:
    return {"error": str(e)}, 500
  


@app.route('/get_tema', methods=["GET"])
def get_tema():
  try:
    fag = request.get_json()["fag"]
    cur.execute("SELECT tema, id FROM tema WHERE fag = ?", (fag,))
    data = cur.fetchall()
    response = []
    for tema in data:
      response.append({"tema": tema[0], "id": tema[1]})

    return response, 200
  except sqlite3.Error as e:
    return {"error": str(e)}, 500

@app.route('/post_tema', methods=["POST"])
def post_tema():
  try:
    tema = request.get_json()["tema"]
    fag = request.get_json()["fag"]

    cur.execute("INSERT INTO tema(tema, fag) VALUES(?, ?)", (tema, fag))
    con.commit()

    return {"melding": "Tema lagt til"}, 200
  except sqlite3.Error as e:
    return {"error": str(e)}, 500


@app.route('/get_guides', methods=["GET"])
def get_guides():
  return Response(status=200)

@app.route('/get_guide', methods=["GET"])
def get_guide():
  return Response(status=200)

@app.route('/post_guide', methods=["POST"])
def post_guides():
  return Response(status=200)



@app.route('/get_kommentarer', methods=["GET"])
def get_kommentarer():
  return Response(status=200)

@app.route('/post_kommentarer', methods=["GET"])
def post_kommentarer():
  return Response(status=200)



if __name__ == "__main__":
  app.run(debug=True, port=5010)