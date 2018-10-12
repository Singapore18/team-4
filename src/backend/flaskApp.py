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
    return jsonify(json_list=[i.serialize for i in QuestionBank.query.all()])
   
@app.route('/response', methods=['POST'])
def postAnswer():
    # print(dir(request))
    data = request.get_data().decode('utf8')
    print(data)
    
    # for response in data["response"]:
    #     print(response)
    #     qid = data["qid"]
    #     sid = data["sid"]
    #     value = data["value"]
    #     kid = data["kid"]
    #     mid = data["mid"]
    #     db.session.add(Response(qid=qid, sid=sid, value=value, kid=kid, mid=mid))
    # db.session.commit()
    
    return jsonify(
        status = 200
    )


@app.route('/response', methods=['GET'])
def getAnswer():
    return jsonify(json_list=[i.serialize for i in Response.query.all()])

@app.route('/postResults', methods=['POST'])
def postResults():
    # try:
    #     _results = request.form['results']
    pass

# @app.route('/questions', methods=['POST'])
# def setResults():
#     return json.dumps(QuestionBank.query.all())

# @app.route('/survey', methods=['GET'])
# def getAllSurveys():
#     return Survey.query.all()

# @app.route('/survey', methods=['GET'])
# def getAllMetrics():
#     return Survey.query.all()

@app.route('/keystone', methods=['GET'])
def getAllKeystone():
    return jsonify(json_list=[i.serialize for i in Keystone.query.all()])

# @app.route('/results', methods=['GET'])
# def getAllResults():
#     return Result.query.all()



if __name__ == "__main__":
    app.run(port=5002)
