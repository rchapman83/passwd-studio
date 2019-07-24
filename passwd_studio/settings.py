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
LOGGING = {
    'version': 1,
    'handlers': {
        'timber': {
            'level': 'INFO',
            'class': 'timber.TimberHandler',
            'api_key': timber_key,
            'source_id': timber_id
        },
    },
    'loggers': {
        'my-app': {
            'handlers': ['timber'],
            'level': 'INFO',
        }
    },
}