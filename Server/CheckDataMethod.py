#!/usr/bin/python
# coding:utf8
#
#   处理客户端传过来的检查项数据
#   一  解密并验证客户端token
#   二  数据入库
#   三  判断是否到达报警阈值并发送报警
#
#
import sys
sys.path.append('..')
from config import config
from Client import AES
import traceback
import json
import datetime
from WeiXinPush import send_weixin_msg


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
def save_data(data, db):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if data['item'] == 'cpu':
        db.save_cpu(data['hostname'],now, data['iowait'], data['user'], data['system'], data['idle'], data['oneLoad'], data['fiveLoad'], data['fifteenLoad'])
    elif data['item'] == 'disk':
        db.save_disk(data['hostname'], now, data['total'], data['used'], data['free'], data['percent'],
                  data['read_count'], data['write_count'], data['read_bytes'], data['write_bytes'],
                  data['read_time'], data['write_time'])

    elif data['item'] == 'memory':
        db.save_memory(data['hostname'], now, data['free'], data['used'], data['available'])

    elif data['item'] == 'network':
        for item in data:
            if item not in ['item', 'hostname', 'token']:
                d = data[item]
                print 'd:',d
                print 'item:',item
                db.save_Network(data['hostname'], now, item, d['sent'], d['recv'])


# 判断是否达到阈值，触发报警
def judge(data):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ## 判断cpu负载
    if data["item"] == "cpu":
        total = data['iowait'] + data['user'] + data['system'] + data['idle']
        v = float(data['iowait']) / total
        if v > 0.3:
            send_weixin_msg(
                "%s iowait %s"%(data["hostname"],v),
                "%s one:%s,five:%s" %(now,data["oneLoad"], data["fiveLoad"]),
                'cpu count:%s ' %(data['count'])
            )
        load = float(data['oneLoad'])/data['count']
        if load >0.8:
            send_weixin_msg(
                "%s 负载高 %s" % (data["hostname"], load),
                "%s one:%s,five:%s" % (now, data["oneLoad"], data["fiveLoad"]),
                'cpu count:%s ' % (data['count'])
            )
    ## 判断磁盘容量
    if data["item"] == "disk":
        for item in data:
            if item not in ['item', 'hostname', 'token']:
                if data[item]['percent'] > 90:
                    send_weixin_msg(
                        "%s %s 目录快满了"%(data['hostname'], item),
                        "目录还剩下%s" %(100 - data[item]['percent']),
                        "请及时处理"
                    )
    ## 可用内存报警
    if data["item"] == "memory":
        if data["percent"] >95:
            send_weixin_msg("%s 内存已经达到%s,内存不足" %(data["hostname"], data["percent"]),
                            "总内存是%s M ,内存不足会引起系统崩溃" %(data["total"]/1024.0/1024),
                            "请及时处理")


def process(json_data, db):
    flag, data = decrypt_verification_data(json_data)
    if flag:
        save_data(data, db)
        judge(data)
