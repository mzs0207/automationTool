#!/usr/bin/python
# coding:utf8
#
#  post 数据到后端
#
import urllib2
import json
from config import config
import AES
import random
import ssl


def post(data, url):
    data['hostname'] = config['hostname']
    data['token'] = config['token']
    encrypt_str = AES.encrypt(str(data))

    post_data = {
        'data': encrypt_str,
        'id': random.randint(1, 10000)
    }
    context = ssl._create_unverified_context()
    request = urllib2.Request(url=config['url']+url, data=json.dumps(post_data))
    response = urllib2.urlopen(request, context = context)
    result = response.read()
    return result