# -*- coding: utf-8 -*-
'''
@Time    : 2023/5/9 4:23
@Author  : FinleyChan
@FileName: ccibe校园网登录认证.py
@Contact : FinleyChan@foxmail.com
'''

import requests
import re
from time import sleep

# 用户名
userId = ""
# 密码
passwd = ""

pre_url = "http://www.msftconnecttest.com/redirect"

response = requests.get(pre_url)
url = response.url.replace("portal", "webauth")
cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)
cookie_str = [f"{key}={value}" for key, value in cookie_dict.items()][0]
host = re.findall("//(.*?)/", url)[0]

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "398",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": f"{cookie_str}",
    "Host": f"{host}",
    "Origin": f"{host}",
    "Referer": f"{url}",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36 Edg/114.0.0.0",
}

data = {
    "hostIp": "http://127.0.0.1:8082/",
    "loginType": "",
    "auth_type": "0",
    "isBindMac1": "1",
    "pageid": "1",
    "templatetype": "1",
    "listbindmac": "1",
    "recordmac": "1",
    "isRemind": "0",
    "isautoauth": "",
    "notice_pic_loop1": "/portal/uploads/pc/demo3/images/logo.jpg",
    "notice_pic_loop2": "/portal/uploads/pc/demo3/images/rrs_bg.jpg",
    "userId": userId,
    "passwd": passwd,
    "twiceauth": "1",
    "isBindMac": "bindmac",
}

while True:
    try:
        response_auth = requests.post(url=url, headers=header, data=data)
        if response_auth.status_code == 200:
            print("认证成功")
            sleep(3)
            break;
    except Exception as e:
        print("认证出错")
        sleep(3)
        break;
