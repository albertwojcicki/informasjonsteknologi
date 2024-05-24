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
    if not data:
      return {"melding": "Fant ikke temaer"}, 404
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
  try:
    tema_id = request.get_json()["tema_id"]
    cur.execute("SELECT id, bruker_navn, tittel, dato FROM guides WHERE tema_id = ?", (tema_id,))
    data = cur.fetchall()
    if not data:
      return {"melding": "Fant ingen guides"}, 404
    response = []
    for guide in data:
      response.append({"id": guide[0], "navn": guide[1], "tittel": guide[2], "dato": guide[3]})

    return response, 200
  except sqlite3.Error as e:
    return {"error": str(e)}, 500

@app.route('/post_guide', methods=["POST"])
def post_guides():
  try:
    tema_id = request.get_json()["tema_id"]
    bruker_id = request.get_json()["bruker_id"]
    bruker_navn = request.get_json()["bruker_navn"]
    innhold = request.get_json()["innhold"]
    tittel = request.get_json()["tittel"]
    dato = datetime.now().strftime("%x %X")
    print(dato)


    cur.execute("INSERT INTO guides(tema_id, bruker_id, bruker_navn, innhold, tittel, dato) VALUES(?,?,?,?,?,?)", (tema_id, bruker_id, bruker_navn, innhold, tittel, dato))
    con.commit()

    return {"melding": "Guide lagt til"}, 200
  except sqlite3.Error as e:
    return {"error": str(e)}, 500

@app.route('/get_guide', methods=["GET"])
def get_guide():
  try:
    guide_id = request.get_json()["guide_id"]
    cur.execute("SELECT id, bruker_id, bruker_navn, tittel, innhold, dato FROM guides WHERE id = ?", (guide_id,))
    data = cur.fetchone()
    print(data)
    if not data:
      return {"error": "Fant ikke guide"}, 404
    
    response = {"id": data[0], "bruker_id": data[1], "navn": data[2], "tittel": data[3], "innhold": data[4], "dato": data[5]}
    return response, 200
  except sqlite3.Error as e:
    return {"error": str(e)}, 500



@app.route('/get_kommentarer', methods=["GET"])
def get_kommentarer():
  try:
    guide_id = request.get_json()["guide_id"]
    print(guide_id)
    cur.execute("""SELECT kommentarer.id, brukere.id, brukere.navn, kommentarer.innhold, kommentarer.rating, kommentarer.dato FROM kommentarer
                 JOIN brukere on brukere.id = kommentarer.bruker_id WHERE kommentarer.guide_id = ?""", (guide_id,))
    kommentarer = cur.fetchall()
    print(kommentarer)
    if not kommentarer:
      return {"melding": "Fant ingen kommentarer"}, 200
    response = []

    for kommentar in kommentarer:
      response.append({"id": kommentar[0], "bruker_id": kommentar[1], "navn": kommentar[2], "innhold": kommentar[3], "rating": kommentar[4], "dato": kommentar[5]})

    return response, 200
  
  except sqlite3.Error as e:
    return {"error": str(e)}, 500

@app.route('/post_kommentar', methods=["POST"])
def post_kommentarer():
  try:
    bruker_id = request.get_json()["bruker_id"]
    guide_id = request.get_json()["guide_id"]
    innhold = request.get_json()["innhold"]
    rating = request.get_json()["rating"]
    dato = datetime.now()

    cur.execute("INSERT INTO kommentarer(bruker_id, guide_id, innhold, rating, dato) VALUES(?,?,?,?,?)", (int(bruker_id), int(guide_id), str(innhold), int(rating), dato))
    con.commit()

    return {"melding": "kommentar lagt til"}, 200

  except sqlite3.Error as e:
    return {"error": str(e)}, 500



if __name__ == "__main__":
  
  app.run(debug=True, port=5010)
