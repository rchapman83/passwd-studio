# -*- coding: utf-8 -*-
# Import password generator
from . import generator
# Import flask stuff
from flask import Flask
from flask_restful import Resource, Api

# Construct application
application = Flask(__name__.split('.')[0])
application.config.from_envvar('FLASK_SETTINGS')
api = Api(application)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')