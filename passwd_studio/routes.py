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
        return {'greeting': 'Hello World'}, 200

class GetKey(Resource):
    def get(self):
        token = generator.mkKey()
        return {'key': token}, 200

class GetPasswd(Resource):
    def get(self, PassLen):
        if PassLen is None:
            PassLen = int(20)
        if PassLen.is_integer() && PassLen > 0:
            passwd = generator.mkPassword(PassLen)
        elif PassLen=='0':
            abort(404, message='Invalid input: INT must be larger than 0.')
        else:
            abort(404, message='Invalid input: ' + PassLen.str() + '. Only type INT accepted.')
        return {'password': passwd}, 200

api.add_resource(GetPasswd, '/', '/len/<int:PassLen>')
api.add_resource(HelloWorld, '/hi')
api.add_resource(GetKey, '/key')