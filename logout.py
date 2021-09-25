""" 
如果使用此脚本登录，中途出现断网，再次登录显示错误码为RD204，可以尝试运行这个程序，利用登录保存的cookie尝试登出
如果登出后，登录还是显示RD204，那就联系运营商客服人工给你登出
就离谱，这登出怎么什么数据都不需要，您完全不验证是吗？
"""

import requests as r
import re
from config import config


def logout(header):
    res = r.get(config.host + config.logoutUrl, headers=header)
    msg = res.text
    pattern = re.compile(r'"msg":"(.*)\b"')
    uniCode = re.findall(pattern, msg)
    return uniCode[0].encode('utf-8').decode('unicode_escape')


header = {
    'User-Agent': config.User_Agent
}
log = logout(header)
print(log)
