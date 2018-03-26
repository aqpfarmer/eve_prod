# Flask app.py
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
Base.metadata.bind = db
DBSession = sessionmaker(bind=db)
session = DBSession()
