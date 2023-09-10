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
import subprocess

# 用户名
userId = ""
# 密码
passwd = ""

# pre_url = "http://www.msftconnecttest.com/redirect"
pre_url = "http://1.1.1.1"

response = requests.get(pre_url)
referer = response.url
url = referer.replace("portal", "webauth")
cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)
# cookie_str = [f"{key}={value}" for key, value in cookie_dict.items()][1]

key = [f"{key}" for key in cookie_dict.keys()][1]
value = [f"{value}" for value in cookie_dict.values()][1]

# cookies = {'': 'null', key: value}
cookies = {key: value}

host = re.findall("//(.*?)/", url)[0]

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "458",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": f"{host}",
    "Origin": f"{host}",
    "Referer": f"{referer}",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36 Edg/114.0.0.0",
}

data = {
    "scheme": "http",
    "serverIp": "tomcat_server:80",
    "hostIp": "http://127.0.0.1:8081/",
    "loginType": "",
    "auth_type": "0",
    "isBindMac1": "1",
    "pageid": "61",
    "templatetype": "1",
    "listbindmac": "1",
    "recordmac": "1",
    "isRemind": "0",
    "url": "http://1.1.1.1",
    "isautoauth": "",
    "notice_pic_loop1": "/portal/uploads/pc/demo3/images/logo.jpg",
    "notice_pic_loop2": "/portal/uploads/pc/demo3/images/rrs_bg.jpg",
    "userId": userId,
    "passwd": passwd,
    "remInfo": "on",
    "isBindMac": "bindmac"
}

if __name__ == '__main__':
    try:
        response_auth = requests.post(url=url, headers=header, data=data, cookies=cookies)
        # connection_stat = os.system('ping www.baidu.com -n 2')
        connection_stat = subprocess.run("ping www.baidu.com -n 3", stdout=subprocess.DEVNULL).returncode
        if connection_stat == 0:
            print("认证成功, 网络已连接！！！")
            sleep(3)
        else:
            raise ConnectionError("connect failed.")
    except ConnectionError:
        print("认证出错！！！")
        sleep(3)
