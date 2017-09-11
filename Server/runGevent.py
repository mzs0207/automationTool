#!/usr/bin/python
#coding:utf8

from gevent.wsgi import WSGIServer
from AutomationServer import app
from config import config

http_server = WSGIServer((config['listen'], config['port']), app, keyfile=config['keyfilename'],
                         certfile=config['certfilename'])
http_server.serve_forever()