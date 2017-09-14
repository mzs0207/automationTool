#!/usr/bin/python
#coding:utf8
import json
import traceback

from flask import Flask, request, jsonify

import Server.CheckDataMethod
from config import config

app = Flask(__name__)


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
        Server.CheckDataMethod.process(request_json)
        response_json['result'] = "success"
    except Exception, e:
        traceback.print_exc()
        print e
        response_json['error'] = e.message
    return jsonify(response_json)


if __name__ == '__main__':
    app.run(debug=config['debug'], host=config['listen'], port=config['port'])
