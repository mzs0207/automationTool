#!/usr/bin/python
#coding:utf8
import json
import traceback

from flask import Flask, request, jsonify

import CheckDataMethod
from config import config
import MySQLHelp

app = Flask(__name__)
db = MySQLHelp.MySQLHelp()

@app.route('/')
def hello_world():
    return 'Hello World!'


#
# 处理客户端检查项数据
#
@app.route('/checkData', methods=['POST'])
def check_data():
    response_json = {}
    try:
        request_str = request.get_data()
        request_json = json.loads(request_str)
        CheckDataMethod.process(request_json, db)
        response_json['result'] = "success"
    except Exception, e:
        traceback.print_exc()
        print e
        response_json['error'] = e.message
    return jsonify(response_json)


if __name__ == '__main__':
    app.run(debug=config['debug'], host=config['listen'], port=config['port'])
