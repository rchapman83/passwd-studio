# -*- coding: utf-8 -*-
# Entry point to bring up the web app

# from os import environ
import os, subprocess

# Boolean 0=gunicorn  1=debug mode
x = os.environ.get('APP_MODE')
# Grab the config filename from enviro var
c = os.environ.get('APP_CONFIG')
# Get which app to run
a = os.environ.get('APP_MODULE')

# Run either Gunicorn or Flask to serve the app
if x=='0':
    print('Starting application server')
    try:
        subprocess.call(['gunicorn', '-c', c, a])
    except RuntimeError as e:
        print('Failed to start-up application server, exiting' + e)
        quit()
elif x=='1':
    print('Starting application in debug mode')
    from flask import Flask
    from passwd_studio import application
    application.run(host='0.0.0.0', port=8080, debug=True)
else:
    print('Invalid start-up configuration in enviro APP_MODE')
    quit()