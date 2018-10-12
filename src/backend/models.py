import os
from app import db


class QuestionBank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(150))
    kid = db.Column(db.Integer)
    mid = db.Column(db.Integer)
    rev = db.Column(db.Boolean)


class Keystone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20))

    def __repr__(self):
        return '<Keystone %r>' % self.description


class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(20))
    kid = db.Column(db.Integer)


class Student(db.Model):
    nric = db.Column(db.String(4), primary_key=True)

    
db.create_all()

keystone1 = Keystone(description='Growth Oriented')
db.session.add(keystone1)
db.session.commit()

import csv
with open('questionbank.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rev = False
        if row[3] == '1':
            rev = True
        db.session.add(QuestionBank(question=row[0], kid=row[1], mid=row[2], rev=rev))
    db.session.commit()