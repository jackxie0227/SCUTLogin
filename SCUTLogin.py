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



# 登录 url https://s2.scut.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=202421017176&user_password=02273513&wlan_user_ip=10.197.216.243&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=5860&lang=zh
# 注销网站：https://s2.scut.edu.cn/