from flask import Flask, jsonify, request, json
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

mysql.init_app(app)

@app.route('/register', methods=['POST','GET'])
def register():
    try:
        _studentID = request.form['studentID']

        if _studentID:
            conn = mysql.connect()
            cursor = conn.cursor()
    except:
        pass

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
