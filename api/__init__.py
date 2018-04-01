# -*- coding: utf-8 -*-
# Entry point to bring up the web app

# Flask mod imports
from flask import Flask
from flask_restful import Resource, Api

# Construct application
application = Flask(__name__.split('.')[0])
application.config.from_envvar('FLASK_SETTINGS')
api = Api(application)

# Import all the views for this web app
from . import routes
