from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'app.db')
db_url = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)

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
keystone2 = Keystone(description='Confident')
keystone3 = Keystone(description='Strategic Thinker')
keystone4 = Keystone(description='Team Player')
keystone5 = Keystone(description='Productive')

db.session.add(keystone1)
db.session.add(keystone2)
db.session.add(keystone3)
db.session.add(keystone4)
db.session.add(keystone5)

metric1 = Metric(description='Mindset', kid=1)
metric2 = Metric(description='Resillience', kid=1)
metric3 = Metric(description='Self-esteem', kid=2)
metric4 = Metric(description='Self-efficacy', kid=2)
metric5 = Metric(description='Curiosity', kid=3)
metric6 = Metric(description='Visioning', kid=3)
metric7 = Metric(description='Inquiry & Exploration', kid=3)
metric8 = Metric(description='Active Emphatic Listening', kid=4)
metric9 = Metric(description='Collaboration', kid=4)
metric10 = Metric(description='Delayed Gratification', kid=5)
metric11 = Metric(description='Productivity', kid=5)

db.session.add(metric1)
db.session.add(metric2)
db.session.add(metric3)
db.session.add(metric4)
db.session.add(metric5)
db.session.add(metric6)
db.session.add(metric7)
db.session.add(metric8)
db.session.add(metric9)
db.session.add(metric10)
db.session.add(metric11)

db.session.commit()
