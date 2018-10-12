from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/register', methods=['POST','GET'])
def register():
    try:
        _studentID = request.form['studentID']

        if _studentID:
            newStudent = studentID(_studentID)
            db.session.add(newStudent)
            db.session.commit()
    except:
        pass

@app.route('/students', methods=['GET'])
def getAllStudents():
    pass


@app.route('/questions', methods=['GET'])
def getAllQuestions():
    questions = db.Table('census', metadata, autoload=True, autoload_with=engine)


@app.route('/survey', methods=['GET'])
def getAllSurveys():
    pass


@app.route('/results', methods=['GET'])
def getAllResults():
    pass


if __name__ == "__main__":
    app.run(port=5002)
