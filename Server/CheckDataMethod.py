#!/usr/bin/python
# coding:utf8
#
#   处理客户端传过来的检查项数据
#   一  解密并验证客户端token
#   二  数据入库
#   三  判断是否到达报警阈值并发送报警
#
#
from config import config
from Client import AES
import traceback
import json


# 解密并验证token
def decrypt_verification_data(ori_data):
    try:
        #print 'ori_data', ori_data
        decrypt_data = AES.decrypt(ori_data['data'])
        print 'decrypt_data', decrypt_data
        decrypt_data = eval(decrypt_data)

        if decrypt_data['token'] != config['token']:
            return False, None
        return True, decrypt_data

    except Exception, e:
        traceback.print_exc()
        return False, None


# 保存数据
def save_data(data):
    pass


# 判断是否达到阈值，触发报警
def judge(data):
    pass


def process(json_data):
    flag, data = decrypt_verification_data(json_data)
    if flag:
        save_data(data)
