#!/usr/bin/python
#coding:utf8
# 微信推送报警信息
import json
import urllib2
import datetime
from config import config
import MySQLdb

# 获取公众号token的接口
WX_TOKEN_URL = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"
# 模板消息推送接口
WX_TEMPLATE_MSG_API = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s"
WX_TEMPLATE_ID=config['WX_TEMPLATE_ID']
print WX_TEMPLATE_ID

WX_APPID = config['WX_APPID']
WX_SECRET = config['WX_SECRET']
USERS=[{'userid':'18621210266','openid':'ofQzPvz-ULZFnvKydittC8hTAGSk'}]


def get_token():
    return 'IzDalt8zGy71PEsg57DPcOgzAFMke_gZqJ6H_iD2iIBahHHY6BbYf4L88ps3FttXoeRZavq9TwivoSCIUCRfmr9X7Qt6nwfMFdWSlnslWCYHOQfRITgykykWKOtO829ROLWdACAROZ'
    url=WX_TOKEN_URL %(WX_APPID,WX_SECRET)
    try:
        request=urllib2.Request(url)
        response=urllib2.urlopen(request)
        data=response.read()
        jdata=json.loads(data)
        return jdata['access_token']
    except Exception,e:
        print e


def get_token_form_db():
    try:
        conn = MySQLdb.connect(host = config['WX_MySQL_Host'], port = config['WX_MySQL_Port'],
                               user= config['WX_MySQL_User'], passwd = config['WX_MySQL_Passwd'])
        cursor = conn.cursor()
        cursor.execute(config['WX_SQL'])
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data[0]
    except Exception,e:
        print e


def send_weixin_msg( title,content,remark,users=USERS):
    if len(users) == 0:
        return
    if config['WX_Token_Source'] == 'db':
        token = get_token_form_db()
    else:
        token= get_token()
    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    template_msg = {
        "first": {
            "value": title,
            "color": "#173177"
        },
        "keyword1": {
            "value": time_str,
            "color": "#173177"
        },
        "keyword2": {
            "value": content,
            "color": "#173177"
        },
        "remark": {
            "value": remark,
            "color": "#173177"
        }
    }

    url=WX_TEMPLATE_MSG_API %(token)
    for user in users:
        payload= {
            "touser":user["openid"],
            "template_id":WX_TEMPLATE_ID,
            "data":template_msg
        }
        request=urllib2.Request(url,json.dumps(payload))
        response=urllib2.urlopen(request)
        print response.read()


if __name__ == '__main__':
    send_weixin_msg('AutoTool 测试','今天天气很好','哈哈哈')