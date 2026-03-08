import re
import requests
import time
import threading
import sys
import ctypes
import subprocess
import os
from pystray import Icon, Menu, MenuItem
from PIL import Image

# ======================= 固定配置 =======================
url = "" #填入事先保存的url地址

campusNetworkWebURL = '' #填入学校校园网登录网站ip

CAMPUS_WIFI_NAMES = [""] # 填入校园网 WIFI 名称

CHECK_INTERVAL = 3600 #检测时间间隔

# ======================================================

# 获取icon(AI编写，解决打包可能出现的问题)
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# 获取当前WIFI名称
def get_current_wifi():
    try:
        result = subprocess.check_output(
            ["netsh", "wlan", "show", "interfaces"],
            encoding="gbk",
            errors="ignore"
        )
        for line in result.split("\n"):
            if "SSID" in line and "BSSID" not in line:
                return line.split(":")[1].strip()
    except:
        pass
    return ""

# 判断是否为校园网
def is_campus_network():
    wifi = get_current_wifi()
    return any(ssid in wifi for ssid in CAMPUS_WIFI_NAMES)

# 调用通知
def show_notification(title, msg):
    try:
        ctypes.windll.user32.MessageBoxW(None, msg, title, 0x40 | 0x1000)
    except Exception:
        pass

# 登陆函数
def login():
    if not is_campus_network():
        return

    try:
        code = requests.get(url, timeout=8).status_code
        if code == 200:
            show_notification("校园网登录", "手动登录成功")
    except Exception:
        pass

# 检测并重新连接
def check_network_loop():
    while True:
        if is_campus_network():
            try:
                response = requests.get(campusNetworkWebURL, timeout=5)
                pattern = re.compile('<title>(.*?)</title>', re.S)
                title = re.findall(pattern, response.text)

                if not title or title[0] != '注销页':
                    requests.get(url, timeout=8)
                    show_notification("校园网自动登录", "登录成功")
            except Exception:
                pass

        # 等待时间
        time.sleep(CHECK_INTERVAL)

# ------------------------- 托盘菜单 -------------------------
class CampusNetworkLoginTray:
    def __init__(self):
        icon_path = get_resource_path("connect.png")
        self.image = Image.open(icon_path)
        self.icon = Icon(
            "校园网自动登录",
            self.image,
            title="校园网自动登录工具",
            menu=Menu(
                MenuItem("手动登录", self.on_reconnect),
                       MenuItem("退出程序", self.on_quit),
            )
        )

    def on_reconnect(self, icon, item):
        login()


    def on_quit(self, icon, item):
        icon.stop()
        sys.exit(0)


    def run(self):
        self.icon.run()


if __name__ == "__main__":

    #后台运行
    threading.Thread(target=check_network_loop, daemon=True).start()
    app = CampusNetworkLoginTray()
    app.run()