from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from models import db
from models import app
from models import Keystone
from models import QuestionBank
from models import Metric

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)

# load questions into questionBank table in DB
# engine = create_engine('sqlite:///cdb.db')
# Base.metadata.create_all(engine)
#
# df = pandas.read_csv("questions.csv")
# df.to_sql(con=engine, name=cdb1.QuestionBank, if_exists='replace')
# df.to_sql(con=engine, index_label='id', name=cdb1.__tablename__, if_exists='replace')

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
    return QuestionBank.query.all()

@app.route('/postResults', methods=['POST'])
def postResults():
    # try:
    #     _results = request.form['results']

    #     if _results:
    #         newResults = Result(result = _results)
    #         db.session.add(newResults)
    #         db.session.commit()
    # except:
    #     pass

@app.route('/survey', methods=['GET'])
def getAllSurveys():
    return Survey.query.all()

@app.route('/survey', methods=['GET'])
def getAllMetrics():
    return Survey.query.all()

@app.route('/keystone', methods=['GET'])
def getAllKeystone():
    return Keystone.query.all()

@app.route('/results', methods=['GET'])
def getAllResults():
    return Result.query.all()



if __name__ == "__main__":
    app.run(port=5002)
