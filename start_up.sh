#!/bin/sh

GUNICORN=/opt/app-root/bin/gunicorn
PROJ=/opt/app-root/src
PID=/var/run/gunicorn.pid

if [ -f $PID ]; then rm $PID; fi

cd $PROJ
exec $GUNICORN -c $PROJ/$APP_CONFIG --pid=$PID $APP_MODULE
