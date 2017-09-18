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

# 实现加密混淆的字符串，长度应该是16或32或64
config['CryptoKey'] = 'jikjhg457hgdetyh'

# 配置mysql ip
config['mysql_ip'] = 'localhost'

# 配置mysql 端口
config['mysql_port'] = 3306

# 配置数据库名
config['database'] = 'autoTool'

# 配置mysql 用户
config['mysql_user'] = 'admin'

# 配置mysql 密码
config['mysql_passwd'] = 'admin'

# 配置微信APPID
config['WX_APPID'] = ''

#配置微信SECRET
config['WX_SECRET'] = ''

#配置微信消息id
config['WX_TEMPLATE_ID'] = ''

