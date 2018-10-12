from flask import Flask, jsonify, request, json
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)


@app.route('/register', methods=['POST','GET'])
def register():
    return "Hello World"

@app.route('/students', methods=['GET'])
def getAllStudents():
    pass


@app.route('/questions', methods=['GET'])
def getAllQuestions():
    pass


@app.route('/survey', methods=['GET'])
def getAllSurveys():
    pass


@app.route('/results', methods=['GET'])
def getAllResults():
    pass


if __name__ == "__main__":
    app.run(port=5002)
