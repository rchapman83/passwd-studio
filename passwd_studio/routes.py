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
        api.logger_timber.info('Test message...hi')
        return {'greeting': 'Hello World'}, 200

class GetKey(Resource):
    def get(self):
        token = generator.mkKey()
        return {'key': token}, 200

class GetPasswd(Resource):
    def get(self):
        try:
            passwd = generator.mkPassword()
        except RuntimeError as e:
            print ('Could not generate password: ' + e)

        return {'password': passwd}, 200

class GetVarLenPasswd(Resource):
    def get(self, PassLen):
        if PassLen.is_integer() and PassLen > 0:
            passwd = generator.mkPassword(PassLen)
        elif PassLen is None:
            abort(404, message='Invalid input: len is null')
        elif PassLen=='0':
            abort(404, message='Invalid input: INT must be larger than 0.')
        else:
            abort(404, message='Invalid input: ' + PassLen.str() + '. Only type INT accepted.')
        return {'password': passwd}, 200

api.add_resource(GetPasswd, '/')
api.add_resource(GetVarLenPasswd, '/len/<int:PassLen>')
api.add_resource(HelloWorld, '/hi')
api.add_resource(GetKey, '/key')