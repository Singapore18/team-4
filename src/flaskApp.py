from flask import Flask, jsonify, request, json
from flask.ext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'jay'
mysql.init_app(app)

@app.route('/')
