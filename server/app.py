from flask import Flask, render_template, request, jsonify, send_from_directory, json, redirect, session
import json
import requests
import sqlite3
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# BYTT PATH PÅ DATABASEN    
con = sqlite3.connect("database.db", check_same_thread=False)
cur = con.cursor()

# @app.route("/")