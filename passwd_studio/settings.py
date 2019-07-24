# -*- settings:utf-8 -*-
# Flask settings

import os, logging, logging.config, timber

# Timber api token and source id
timber_key = os.environ.get('TIMBER_TOKEN')
timber_id = os.environ.get('TIMBER_ID')
proj_name = os.environ.get('PROJECT_NAME')
secret_code = os.environ.get('FLASK_SECRET')

# Base config
DEBUG = False
TESTING = False
USE_X_SENDFILE = False
CSRF_ENABLED = True
APPLICATION_ROOT = '/'
SERVER_NAME = None
#SERVER_NAME = 'api.passwd.studio:8080'
SECRET_KEY = secret_code
PREFERRED_URL_SCHEME = 'http'

# Cookie settings
SESSION_COOKIE_NAME = 'session'
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_PATH = None
SESSION_COOKIE_HTTPONLY = True

# JSON & Jsonify 
JSON_AS_ASCII = True
JSON_SORT_KEYS = True

# LOGGING
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logger_timber = logging.getLogger(__name__)
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
timber_handler = timber.TimberHandler(source_id=timber_id, api_key=timber_key, level=LOG_LEVEL, buffer_capacity=20, flush_interval=60, raise_exceptions=True)
logger_timber.addHandler(timber_handler)
LOGGER_NAME = 'logger_timber