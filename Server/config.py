#!/usr/bin/python
# coding:utf8
#
# 配置文件
#

config = {}

##服务监听端口
config['port'] = 15789

## 服务监听ip
config['listen'] = ''

## 是否开启调试模式，开启调试模式请运行AutomationServer.py，正常请执行runGevent.py
config['debug'] = False

# 支持https，配置证书和key
config['keyfilename'] = 'server.key.unsecure'

config['certfilename'] = 'server.crt'

# token，验证服务端与客户端传输数据是否匹配
config['token'] = 'hahaha'

# 实现加密混淆的字符串
config['CryptoKey'] = 'joiiasfiejaklfd'


