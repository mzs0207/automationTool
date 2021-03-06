#!/usr/bin/python
# coding:utf8
#
# 配置文件
#

config = {}

# 是否开启使用https
config['https'] = False

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
config['WX_TEMPLATE_ID'] = 'GUZtolJh81Ic-hTL9uv_ELH_mpL04VEsciAzGWSOLm4'

# 当配置微信推送token 来自数据库的时候
config['WX_Token_Source'] = 'db'
config['WX_MySQL_Host'] = ''
config['WX_MySQL_Port'] = ''
config['WX_MySQL_User'] = ''
config['WX_MySQL_Passwd'] = ''
config['WX_SQL'] = "select access_token,expire_date from stock_app.t_weixin_access_token where appid='wxe031013412e9afdb';"

