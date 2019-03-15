from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                    os.path.join(basedir, 'database.db')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(server)


@server.route('/')
def index():
    return "Hello World"


if __name__ == "__main__":
    server.run(debug=True)
