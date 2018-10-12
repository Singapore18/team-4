from flask import Flask, jsonify, request, json
from flask.ext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

mysql.init_app(app)

@app.route('/students', methods=['POST'])
def getAllStudents():

@app.route('/questions', methods=['POST'])
def getAllQuestions():

@app.route('/survey', methods=['POST'])
def getAllSurveys():

@app.route('/results', methods=['POST'])
def getAllResults():

