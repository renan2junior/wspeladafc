from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fmhzdkydplntpk:5T48echycwSCoT0gz_jrLTFSSf@ec2-54-235-102-190.compute-1.amazonaws.com:5432/d1guckdvshp25u'
db = SQLAlchemy(app)


class ValidationError(ValueError):
    pass
