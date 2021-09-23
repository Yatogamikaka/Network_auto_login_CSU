host = "http://10.255.255.11:801"
# 主机ip
referer = "http://10.255.255.11/"
# 重定向ip
bili = "https://bilibili.com/"
# 叔叔的网站
userName = ""
# 用户名
password = ""
# 登陆密码
operators = ""
# 运营商 中国移动：cmcc 中国联通：cucc 中国电信：ctcc
loginApi = "/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account={}%40{}&user_password={}&wlan_user_ip=10.36.48.120&wlan_user_ipv6=&wlan_user_mac=4CEDFBA87C67&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.2".format(
    userName, operators, password)
# 登陆接口
sidApi = "/eportal/?c=Portal&a=page_type_data&callback=dr1001"
# cookie接口
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
# 模拟浏览器
