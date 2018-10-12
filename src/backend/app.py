from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'app.db')
db_url = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)