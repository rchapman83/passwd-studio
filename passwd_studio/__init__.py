# -*- coding: utf-8 -*-
# Entry point to bring up the web app
# Import Flask stuff
from flask import Flask
from flask_restful import Resource, Api

# Construct application
application = Flask(__name__.split('.')[0])
application.config.from_envvar('FLASK_SETTINGS')
#logger_timber.info('load flask app')
# Import all the views for app
from . import routes