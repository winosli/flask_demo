from flask import Flask
from flask_restful import Api, reqparse
from flask_jwt import JWT

# from security import authenticate, identity
from resources.app import App, AppList
from models.app import AppModel
import os

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('sqlite:///' + os.path.join(basedir, 'db.sqlite'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data.db'))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
#app.secret_key = 'jose'
api = Api(app)

# Use this to create the table
# @app.before_first_request
# def create_tables():
#     db.create_all()

#jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(App, '/app/<string:_id>')
api.add_resource(AppList, '/apps')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

