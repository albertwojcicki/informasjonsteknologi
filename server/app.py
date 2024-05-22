from flask import Flask, request
import sqlite3
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

con = sqlite3.connect("database.db", check_same_thread=False)
cur = con.cursor()


@app.route('/get_tema')
def get_tema():
  return 200
