# 写一个自动登陆 http://shanxitobacco.com 的小程序，自动下载每次最新的csv文件
# 自动登录，代码是 星火ai写的，不对，大多数是我自己写的
# 创建于2024-01-02，最后修改时间是240102晚8点，烂尾了，又烂尾了，之后再完善吧
# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

# 替换为你的用户名和密码
username = input("input your username:")
password = input("input your password:")
# password = input("Input your password:")

# 替换为网站的URL
url = "https://shanxitobacco.com/wdk?action=ecw.page&method=display&page_id=page_login&site_id=web"

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()

# 打开网站
driver.get(url)

# 定位用户名输入框并输入用户名
# username_input = driver.find_element_by_name("username")
username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(username)

# 定位密码输入框并输入密码
# password_input = driver.find_element_by_name("userpwd")
password_input = driver.find_element(By.NAME, "userpwd")
password_input.send_keys(password)

# 预留10秒用来手动输入验证码
time.sleep(10)

# 按下回车键进行登录
password_input.send_keys(Keys.RETURN)

# 等待页面加载完成（根据实际情况调整等待时间）
driver.implicitly_wait(10)

# 模拟点击进入我的订购
button1 = driver.find_element(By.XPATH, "//*[@id='web_header']/div/div/ul[1]/li[2]/a")
button1.click()
driver.implicitly_wait(3)

# 找到最新的账单，点击订单详情
button2 = driver.find_element(By.XPATH, "//*[@id=‘m_order_wrap’]/div[1]/div/div[7]/div/a")
button2.click()
driver.implicitly_wait(3)

# 点击导出按钮
button3 = driver.find_element(By.XPATH, "//*[@id='export_xls_btn']")
button3.click()

time.sleep(15)
# 关闭浏览器
driver.quit()


''' 有点复杂，放弃下面这些代码了
# 登录页面的URL
login_url = 'https://shanxitobacco.com/wdk?action=ecw.page&method=display&page_id=page_login&site_id=web'

password = input("请输入密码：")
# 用户名和密码
payload = {
    'login_username': 'your_username',
    'login_userpwd': password
}

# 创建一个session对象，用于保持登录状态
session = requests.Session()

# 获取登录页面的内容
response = session.get(login_url)
soup = BeautifulSoup(response.text, 'html.parser')

# 查找登录表单中的CSRF令牌
csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

# 更新payload中的CSRF令牌
payload['csrf_token'] = csrf_token

# 提交登录表单
response = session.post(login_url, data=payload)

# 检查是否登录成功
if response.url == 'https://www.shanxitobacco.com/dashboard':
    print('登录成功')
else:
    print('登录失败')
'''
