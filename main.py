from config import config
import requests as r
import webbrowser as web


class network():
    def __init__(self, localHost, loginApi, ssidApi) -> None:
        self.api = localHost
        self.loginUrl = loginApi
        self.ssidUrl = ssidApi

    def get(self, url, header):
        return r.get(self.api + url, headers=header)

    def getSid(self, UC) -> str:

        header = {
            'Connection': 'keep-alive',
            'User-Agent': UC
        }

        res = self.get(self.ssidUrl, header)
        netCookie = {}
        for ck in res.cookies:
            netCookie[ck.name] = ck.value
        str = "PHPSESSID={}".format(netCookie.get('PHPSESSID'))
        with open("config\PHPSESSID.txt", "w") as f:
            f.write(str)
        return str

    def login(self, header) -> bool:
        res = self.get(self.loginUrl, header)
        if res.status_code == 200:
            return True
        else:
            return False


if __name__ == '__main__':
    host = config.host
    loginUrl = config.loginUrl
    ssidUrl = config.ssidUrl
    UC = config.User_Agent
    bili = config.bili
    refer = config.referer

    net = network(host, loginUrl, ssidUrl)
    ssid = net.getSid(UC)
    header = {
        'Connection': 'keep-alive',
        'User-Agent': UC,
        'Cookie': "PHPSESSID={}".format(ssid)
    }
    if net.login(header):
        # web.open(refer)
        web.open(bili)
    else:
        web.open(refer)
