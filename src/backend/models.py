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
db.session.add(keystone1)
db.session.commit()
