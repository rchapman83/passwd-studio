# -*- settings:utf-8 -*-
# Flask settings

import os, logging, logging.config, timber

# Timber api token and source id
timber_key = os.environ.get('TIMBER_TOKEN')
timber_id = os.environ.get('TIMBER_ID')
proj_name = os.environ.get('PROJECT_NAME')
secret_code = os.environ.get('FLASK_SECRET')

DEBUG = False
TESTING = False
USE_X_SENDFILE = False
CSRF_ENABLED = True
SECRET_KEY = secret_code

# LOGGING
LOGGER_NAME = 'logger_timber'
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
#timber_handler = timber.TimberHandler(source_id=timber_id, api_key=timber_key, level=logging.INFO, buffer_capacity=20, flush_interval=60, raise_exceptions=True)
logger_timber.addHandler(timber_handler)