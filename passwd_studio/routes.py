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
        return {'hello': 'world'}, 200

class GetKey(Resource):
    def get(self):
        token = mkKey();
        return {'key': token}, 200

api.add_resource(HelloWorld, '/', '/hi')
api.add_resource(GetKey, '/key')