# by jackxie
# 获取 url 登录信息
from Prepare import prepare
account, password, wlan_user_ip, wlan_ac_ip = prepare()
print("登录中...\n")

# url
url = "https://s2.scut.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account={}&user_password={}&wlan_user_ip={}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip={}&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=5860&lang=zh"
url = url.format(account, password, wlan_user_ip, wlan_ac_ip)

# 登入网址
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
driver_path = "scut-students-login/msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service)

try:
    driver.get(url)
finally:
    driver.quit()


import requests
def test_network():  
    try:  
        response = requests.get('https://www.baidu.com', timeout=1)  
        if response.status_code == 200:  
            print('网络连接正常。')  
        else:  
            print(f'网络连接异常，状态码：{response.status_code}')  
    except requests.exceptions.RequestException as e:  
        print(f'网络连接异常：{e}')  

# 在登录成功后调用测试函数  
test_network()

# 登录 url https://s2.scut.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=202421017176&user_password=02273513&wlan_user_ip=10.197.220.30&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=192.168.53.174&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=5860&lang=zh
# 登录成功 url https://s2.scut.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=202421017176&user_password=02273513&wlan_user_ip=10.197.220.194&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=192.168.53.174&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=6281&lang=zh
# 注销网站：https://s2.scut.edu.cn/
# 登录页面：https://s2.scut.edu.cn/a79.htm?userip={}&wlanacname=&wlanacip=192.168.53.174