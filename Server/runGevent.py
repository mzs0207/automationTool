#!/usr/bin/python
#coding:utf8

from gevent.wsgi import WSGIServer
from AutomationServer import app
from config import config

if config['https']:
    http_server = WSGIServer((config['listen'], config['port']), app, keyfile=config['keyfilename'],
                         certfile=config['certfilename'])
else:
    http_server = WSGIServer((config['listen'], config['port']), app)
http_server.serve_forever()