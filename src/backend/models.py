from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class QuestionBank(db.Model):
    qid = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(150))
    kid = db.Column(db.Integer)
    mid = db.Column(db.Integer)
    rev = db.Column(db.Boolean)


class Keystone(db.Model):
    kid = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20))


class Metric(db.Model):
    mid = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20))
    kid = db.Column(db.Integer)



class Student(db.Model):
    nric = db.Column(db.String(4), primary_key=True)

    

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

