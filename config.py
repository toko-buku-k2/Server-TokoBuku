from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect( app):
    db.init_app(app)

class Config:
    SQLALCHEMY_DATABASE_URI= 'postgresql://postgres:5127@localhost/bukuku'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER= "static/upload"