from flask import Flask
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import Session
from models import Brand, Country, Phone
basedir = os.path.abspath(os.path.dirname(__file__))
server = Flask(__name__)
engine = create_engine('sqlite:///' + os.path.join(basedir, 'database.db'), echo=False)
session = Session(bind=engine)


@server.route('/')
def index():
    return "Hello World"


if __name__ == "__main__":
    server.run(debug=True)
