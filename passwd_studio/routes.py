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
        return {'greeting': 'Hellow World'}, 200

class GetKey(Resource):
    def get(self):
        token = generator.mkKey()
        return {'key': token}, 200

class GetPasswd(Resource):
    def get(self):
        passwd = generator.mkPassword();
        return {'password': passwd}, 200

api.add_resource(GetPasswd, '/')
api.add_resource(HelloWorld, '/hi')
api.add_resource(GetKey, '/key')