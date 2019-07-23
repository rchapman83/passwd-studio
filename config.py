# -*- config:utf-8 -*-
# make Gunicorn work good and stuff

import multiprocessing

bind = '0.0.0.0:8080'
name = 'passwd-studio'
backlog = 2048
max_requests = 1000
proc_name = 'passwd-studio'
workers = int((multiprocessing.cpu_count() * 2) + 1)
threads = int(multiprocessing.cpu_count()+1)
daemon = False
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

forwarded_allow_ips = '*'
# secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
