# -*- coding: utf-8 -*-
# Entry point to bring up the web app

# from os import environ
import os, subprocess, logging, logging.config, timber


# Boolean 0=gunicorn  1=debug mode
x = os.environ.get('APP_MODE')
# Grab the config filename from enviro var
c = os.environ.get('APP_CONFIG')
# Get which app to run
a = os.environ.get('APP_MODULE')
# Timber api token
t = os.environ.get('TIMBER_TOKEN')

#log_format = '%(asctime)s - %(message)s'
#logging.basicConfig(level=logging.INFO, format=log_format)
#logger = logging.getLogger()
#timber_handler = timber.TimberHandler(api_key=t, level=logging.INFO, buffer_capacity=20, flush_interval=60, raise_exceptions=True)
#logger.addHandler(timber_handler)

# Run either Gunicorn or Flask to serve the app
if x=='0':
    print('Starting application server')
    try:
        subprocess.call(['gunicorn', '-c', c, a])
        #logger.debug('gunicorn start-up complete')
    except RuntimeError as e:
        print('Failed to start-up application server, exiting')
        #logger.error('Failed to start-up gunicorn, exiting. Consider putting application into debug mode' + e)
        quit()
elif x=='1':
    print('Starting application in debug mode')
    #logger.debug('Starting flask app server in debug mode')
    from flask import Flask
    from passwd_studio import application
    application.run(host='0.0.0.0', port=8080, debug=True)
else:
    print('Invalid start-up configuration')
    #logger.critical('Invalid start-up configuration for run.py, quitting')
    quit()
