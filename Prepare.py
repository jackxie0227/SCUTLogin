import os 
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


folder_name = 'scut-students-login'
credentials_file = os.path.join(folder_name, 'credentials.txt')
driver_path = os.path.join(folder_name, "msedgedriver.exe")

account = None
password = None

# 创建自定义对话框类
class CredentialsDialog(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=None)
        
        # 对话框标题 --- "scut-student 账号信息输入"
        self.title("输入凭据") 
        self.geometry("300x200")  # 设置对话框的初始大小为300x200像素  
        
        # 创建标签和输入框
        tk.Label(self, text="学号:").pack(pady=5)
        self.account_entry = tk.Entry(self)
        self.account_entry.pack(pady=5)
        
        tk.Label(self, text="密码:").pack(pady=5)
        self.password_entry = tk.Entry(self)
        self.password_entry.pack(pady=5)
        
        # 创建确认按钮
        self.submit_button=tk.Button(self,text="确认",command=self.submit)
        self.submit_button.pack(pady=10)
        
        self.account=None
        self.password=None
        
    def submit(self):
        # 获取账号 密码
        self.account = self.account_entry.get()
        self.password = self.password_entry.get()
        
        # 关闭对话框
        self.destroy()
        

# 在当前目录创建文件夹和文件的函数
def create_credentials_file(folder_name, account, password, wlan_user_ip, wlan_ac_ip):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    with open(os.path.join(folder_name, 'credentials.txt'), 'w') as f:
        f.write(f"{account}\n{password}\n{wlan_user_ip}\n{wlan_ac_ip}")

# 获取主机、服务器ip地址
import socket  
def get_ip():   
    hostname = socket.gethostname()  
    wlan_user_ip = socket.gethostbyname(hostname)  
    wlan_ac_ip = "192.168.53.174"
    return wlan_user_ip, wlan_ac_ip


import subprocess, os
def is_connectted_student_scut():
    # 检查是否已经连接到 "scut-student"
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
        if "SSID" in result.stdout:
            for line in result.stdout.splitlines():
                if "SSID" in line:
                    ssid = line.split(":")[1].strip()  # 获取SSID  
                    if ssid == "scut-student":  
                        return True
        return False
    except Exception as e:
        print(f"检测 WI-FI 连接时出错: {e}")
        return False
def connect_student_scut():
    try:
        # 搜索可用的 WI-FI 网络
        result = subprocess.run(['netsh', 'wlan', 'show', 'network'], capture_output=True, text=True)  
        
        if "scut-student" in result.stdout:  
            print("找到 'scut-student' Wi-Fi, 正在连接...")  
            
            connect_result = subprocess.run(['netsh', 'wlan', 'connect', 'name=scut-student'], capture_output=True, text=True)  
            if "成功" in connect_result.stdout:  
                print("成功连接到 'scut-student' Wi-Fi。")  
            else:  
                print("连接 'scut-student' Wi-Fi 失败。")  
        else:  
            print("未找到 'scut-student' Wi-Fi。")
    except Exception as e:  
        print(f"连接Wi-Fi时出错: {e}")

# 主程序
def prepare():
    # 检查驱动文件是否存在
    if not os.path.exists(driver_path):
        messagebox.showwarning("驱动缺失", "请下载 edge 驱动")
        
    # 确保已连接至 scut-student
    if is_connectted_student_scut():
        print("已连接到 scut-student")
    else:
        print("正在连接至 scut-student")
        connect_student_scut()
        
    
    
    # 检查是否存在凭据文件
    if os.path.exists(credentials_file):
        with open(credentials_file, 'r') as f:
            account = f.readline().strip()
            password = f.readline().strip()
            wlan_user_ip = f.readline().strip()
            wlan_ac_ip = f.readline().strip()
        print("已加载账户信息: ")
        print(f"账户名   : {account}")
        print(f"密码     : {password}")
        
        # 重新单独获取用户地址（可能会变）
        wlan_user_ip, _ = get_ip()
    else:
        root = tk.Tk()
        root.withdraw() # 隐藏主窗口
        
        # 显示对话框
        dialog = CredentialsDialog(root)
        root.wait_window(dialog)
        
        # 获取用户输入
        account = dialog.account
        password = dialog.password
        wlan_user_ip, wlan_ac_ip = get_ip()
        
        # 保存用户信息
        create_credentials_file(folder_name, account, password, wlan_user_ip, wlan_ac_ip)
        print('账户信息已保存')
        print(f"账户名 : {account}")
        print(f"密码   : {password}")
        
    return account, password, wlan_user_ip, wlan_ac_ip
        
if __name__ == "__main__":  # 检查当前模块是否为主程序  
    prepare()  # 调用主程序函数      