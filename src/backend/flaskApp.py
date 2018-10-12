from flask import Flask, jsonify, request, json

from models import QuestionBank
from models import Keystone
from models import QuestionBank
from models import Metric
from models import Student
from models import Response
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
    # questions = QuestionBank.query.all()
    return jsonify(json_list=[i.serialize for i in QuestionBank.query.all()])
    # print(QuestionBank.query.all())
    # return "hi"
    # return json.dumps(QuestionBank.query.all())

@app.route('/postResults', methods=['POST'])
def postResults():
    # try:
    #     _results = request.form['results']
    pass

@app.route('/questions', methods=['POST'])
def setResults():
    return json.dumps(QuestionBank.query.all())

# @app.route('/survey', methods=['GET'])
# def getAllSurveys():
#     return Survey.query.all()

# @app.route('/survey', methods=['GET'])
# def getAllMetrics():
#     return Survey.query.all()

@app.route('/keystone', methods=['GET'])
def getAllKeystone():
    return jsonify(json_list=[i.serialize for i in Keystone.query.all()])

@app.route('/results', methods=['GET'])
def getAllResults():
    return Result.query.all()

@app.route('/score', methods=['GET'])
def getScore():
    score = {
           'g1' : 0,
           'g2' : 0,
           'c1' : 0,
           'c2' : 0,
           's1' : 0,
           's2' : 0,
           's3' : 0,
           't1' : 0,
           't2' : 0,
           'p1' : 0,
           'p2' : 0,

       }

    listOfResponses = [i.serialize for i in Response.query.all()]
    for reponses in listOfResponses:
        for m,n in score.items():
            if responses['mid'] == m:
                score[m] += responses['value']

    return json.dumps(score, ensure_ascii=False)

if __name__ == "__main__":
    app.run(port=5002)
