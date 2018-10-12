from flask import Flask, jsonify, request, json

from models import QuestionBank
from models import Keystone
from models import QuestionBank
from models import Metric
from models import Student
# from models import Survey

from app import db, app

@app.route('/register', methods=['POST','GET'])
def register():
    # try:
    #     _nric = request.form['nric']

    #     if _studentID:
    #         newStudent = Student(nric = _nric)
    #         db.session.add(newStudent)
    #         db.session.commit()
    # except:
    #     pass
    return "hello world"

@app.route('/students', methods=['GET'])
def getAllStudents():
    return Student.query.all()


@app.route('/questions', methods=['GET'])
def getAllQuestions():
    questions = QuestionBank.query.all()
    return jsonify([QuestionBank.serialize(question) for question in questions])
    # print(QuestionBank.query.all())
    # return "hi"
    # return json.dumps(QuestionBank.query.all())

@app.route('/questions', methods=['POST'])
def setSurvey():
    return QuestionBank.query.all()

@app.route('/questions', methods=['POST'])
def setResults():
    return json.dumps(QuestionBank.query.all())

# @app.route('/survey', methods=['GET'])
# def getAllSurveys():
#     return Survey.query.all()

# @app.route('/survey', methods=['GET'])
# def getAllMetrics():
#     return Survey.query.all()

# @app.route('/survey', methods=['GET'])
# def getAllKeystone():
#     return Keystone.query.all()


@app.route('/results', methods=['GET'])
def getAllResults():
    return Result.query.all()



if __name__ == "__main__":
    app.run(port=5002)
    

print(getAllKeystone())