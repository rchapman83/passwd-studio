# -*- coding: utf-8 -*-
# All the views here

# Import app via circular imports
from . import application
# Import password generator
from . import passwd
# Import flask stuff
from flask import Flask
from flask_restful import Resource, Api 

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
\api.add_resource(HelloWorld, '/')