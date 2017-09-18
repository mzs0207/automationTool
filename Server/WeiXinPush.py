#!/usr/bin/python
#coding:utf8
# 微信推送报警信息
import json
import urllib2
import datetime
from config import config

# 获取公众号token的接口
WX_TOKEN_URL = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"
# 模板消息推送接口
WX_TEMPLATE_MSG_API = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s"
WX_TEMPLATE_ID=config['WX_TEMPLATE_ID']

WX_APPID = config['WX_APPID']
WX_SECRET = config['WX_SECRET']
USERS=[{'userid':'18621210266','openid':'ofQzPvz-ULZFnvKydittC8hTAGSk'}]


def get_token():
    url=WX_TOKEN_URL %(WX_APPID,WX_SECRET)
    try:
        request=urllib2.Request(url)
        response=urllib2.urlopen(request)
        data=response.read()
        jdata=json.loads(data)
        return jdata['access_token']
    except Exception,e:
        print e


def send_weixin_msg( title,content,remark,users=USERS):
    if len(users) == 0:
        return
    token=get_token()
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


