# 模拟输入账号信息并点击登录
from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys  
import time
import requests

# 初始化 Edge WebDriver  
from selenium.webdriver.edge.service import Service
driver_path = "scut-students-login/msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service)

from Prepare import prepare
account, password, wlan_user_ip, wlan_ac_ip = prepare()

login_url = "https://s2.scut.edu.cn/a79.htm?userip={}&wlanacname=&wlanacip={}".format(wlan_user_ip, wlan_ac_ip)


def py_click():
    # 打开登录页面
    driver.get(login_url)
    time.sleep(0.3)

    # 输入用户名
    try:
        username_input = driver.find_element(By.XPATH, "//input[@name='DDDDD' and @type='text']")
        username_input.clear()
        username_input.send_keys(account)
    except:
        print('您已成功登录或网页有误')
        return

    # 输入密码
    password_input = driver.find_element(By.XPATH, "//input[@name='upass' and @type='password']")
    password_input.clear()
    password_input.send_keys(password)

    # 点击登录按钮
    login_button = driver.find_element(By.XPATH, "//input[@value='登录 / Login']")
    login_button.click()
    
    driver.quit()

    # 检查是否登录成功
    try:  
        response = requests.get('https://www.baidu.com', timeout=1)  
        if response.status_code == 200:  
            print('网络连接正常。')  
        else:  
            print(f'网络连接异常，状态码：{response.status_code}')  
    except requests.exceptions.RequestException as e:  
        print(f'网络连接异常：{e}')  


if __name__ == "__main__":
    py_click()

# 注销网站：https://s2.scut.edu.cn/
# 登录页面：https://s2.scut.edu.cn/a79.htm?userip={}&wlanacname=&wlanacip=192.168.53.174
