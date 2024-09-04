
import requests
from lxml import etree

url = input("please input url:")
response = requests.get(url)
html = etree.HTML(response.text)

title = html.xpath('//*[@id="_tl_editor"]/div[1]/h1')
data = html.xpath('//*[@id="_tl_editor"]/div[1]/p/text()')
print(data)

with open('article.txt', 'w', encoding='utf-8') as f:
    # f.write(str(title) + '\n')
    for item in data:
        f.write(item.text + '\n')

print("Download finished! Over!!!\n")
