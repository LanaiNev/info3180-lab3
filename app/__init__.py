from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "ThisIsMyRandomKey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://giecshymhtduox:bba28f781cb3ae70bf1bb651db4d41159157b68128bd4abc93eee5c2bc0d1396@ec2-23-23-241-119.compute-1.amazonaws.com:5432/dcsmqdn0b5k4th"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project:password123@localhost/project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'


db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
