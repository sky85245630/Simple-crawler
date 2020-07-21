import requests
from bs4 import BeautifulSoup
import html5lib

resp = requests.get('https://sky85245630.github.io/waterfall-html/')
soup = BeautifulSoup(resp.text, 'html5lib')

# 印出這個網址裡面“h1”的純文字
# print(soup.find('h1').text)

# # 用for找到裡面所有的a物件
# for asd in soup.find_all('div'):
#     print(asd)
#     # 找到div裡面的a連結
#     print(asd.a)

# 找到span裡面的waterfall_text class
# for zxc in soup.find_all('span','waterfall_text'):
#     print(zxc)

#用key-value取得網頁中的元素資料
# for qwe in soup.find_all('span',{'class':'waterfall_text'}):
#     print(qwe)

#使用stripped_strings留下純文字
for report in soup.find_all('div','report_sort_box'):
    # print(report)
    for report in report.stripped_strings:
        print(report)