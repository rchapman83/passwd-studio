# -*- coding: utf-8 -*-
# Import password application and generator functions
from . import application
from . import generator
# Import flask stuff
from flask import Flask
from flask_restful import Resource, Api

api = Api(application)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')