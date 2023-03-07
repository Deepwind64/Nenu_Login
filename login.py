import time
import sys
import urllib3
from retrying import retry
from win10toast import ToastNotifier
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
# 作者：Deepwind64
# 版本：V1.0
# 更改时间：2023/2/13 22:37
# 本程序遵循MIT开源协议

# 数据初始化
t1 = time.time()
nenu = 'http://10.100.100.67/'
baidu = 'https://www.baidu.com'
un = ''
pw = ''
notification = ToastNotifier()

# TODO 加入低质量网络处理方案
def net_tester(url):
    try:
        html = urllib3.PoolManager()
        html.request('Get', url, timeout=0.25)
        return True
    except Exception:
        return False


def browser_login(un, pw):
    @retry(wait_fixed=10, stop_max_attempt_number=3)
    def firstFind():
        return browser.find_element(By.XPATH, '//*[@id="username"]')

    def check_up():
        info = '0'
        try:
            # FIXME 等待窗口显示，需优化
            time.sleep(1)
            info = browser.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[2]').text
        except:
            pass
        # print(info)
        if info == '0':
            return
        elif info == "E2901:(ThirdParty1)LDAPPasswordVerificationError":
            notification.show_toast("Nenu Login", "密码错误\n请通过“安装.bat“重设密码", duration=10, threaded=True)
        elif info == "用户不存在":
            notification.show_toast("Nenu Login", "用户不存在\n请通过“安装.bat“重设学号", duration=10, threaded=True)
        else:
            notification.show_toast("Nenu Login", "出现未知异常，请检查代码或网站", duration=10, threaded=True)
        sys.exit()

    browser.get(nenu)
    firstFind().send_keys(un)
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(pw)
    browser.find_element(By.XPATH, '//*[@id="login"]').click()
    check_up()


if __name__ == '__main__':
    if net_tester(baidu):
        notification.show_toast("Nenu Login", "网络已连接", duration=10, threaded=True)
        sys.exit()
    elif net_tester(nenu):
        notification.show_toast("Nenu Login", "网络登录中...", duration=3, threaded=True)
    else:
        notification.show_toast("Nenu Login", "未连接到校园网,等待连接\n15秒后重新登录", duration=10, threaded=True)
        time.sleep(15)
        if net_tester(nenu):
            notification.show_toast("Nenu Login", "网络登录中...", duration=3, threaded=True)
        else:
            notification.show_toast("Nenu Login", "未连接到校园网,登录失败", duration=5, threaded=True)
            sys.exit()
    # TODO 密码文件数据加密
    with open("info.txt", encoding='utf-8') as f:
        un = f.readline().strip()
        pw = f.readline().strip()

    options = Options()
    options.page_load_strategy = 'eager'
    options.add_argument("headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    path = Service(r".\src\msedgedriver.exe")
    browser = webdriver.Edge(service=path, options=options)
    max_try = 3
    count = 0
    while count < max_try:
        try:
            browser_login(un, pw)
            time.sleep(1)
            for i in range(2):
                if net_tester(baidu) is True:
                    total = time.time() - t1
                    notification.show_toast("Nenu Login", "网络连接成功\n用时：{:.2f}s".format(total), duration=2, threaded=True)
                    sys.exit()
        except Exception as e:
            # print(e)
            notification.show_toast("Nenu Login", f"第{count + 1}次连接失败", duration=3, threaded=True)
        count += 1
    notification.show_toast("Nenu Login", "超过最大重试次数，网络连接失败", duration=3, threaded=True)
