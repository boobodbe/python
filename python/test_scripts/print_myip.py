# print myip
# https://www.myexternalip.com/raw

import urllib.request
import requests
from lxml import etree

url = 'http://myexternalip.com/raw'
r = requests.get(url)
ip = r.text
print(ip, type(ip))
# 返回一个str字符串，ipv6地址

url = 'http://myexternalip.com/raw'
# myip = urllib.urlopen(url).read()
myip = urllib.request.urlopen(url).read()
print(myip, type(myip))
# 返回一个二进制地址，ipv6地址

# 用xpath截取网页上的ipv4地址
url = "https://www.myexternalip.com/raw"
myip = requests.get(url)
html = myip.content.decode('utf-8')
print(html)
# 上面这行就可以打印出ipv4地址
# resp = etree.HTML(html)
# ipv4 = resp.xpath('//html/body/pre')
# print(ipv4, type(ipv4))
