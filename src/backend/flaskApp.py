from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask("FlaskApp.py")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/register', methods=['POST','GET'])
def register():
    try:
        _nric = request.form['nric']

        if _studentID:
            newStudent = Student(nric = _nric)
            db.session.add(newStudent)
            db.session.commit()
    except:
        pass

@app.route('/students', methods=['GET'])
def getAllStudents():
    return Student.query.all()


@app.route('/questions', methods=['GET'])
def getAllQuestions():
    return QuestionBank.query.all()


@app.route('/survey', methods=['GET'])
def getAllSurveys():
    return Survey.query.all()

@app.route('/survey', methods=['GET'])
def getAllMetrics():
    return Survey.query.all()

@app.route('/survey', methods=['GET'])
def getAllKeystone():
    return Survey.query.all()


@app.route('/results', methods=['GET'])
def getAllResults():
    return Result.query.all()


if __name__ == "__main__":
    app.run(port=5002)
