# coding:utf-8
# 爬页面元素page_source
from selenium import webdriver
import time
import re
driver = webdriver.Chrome()
driver.get("https://m.fybanks.cn/appstatic/appindex/in/index.html")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
page = driver.page_source
# print(page)

# "非贪婪匹配,re.S('.'匹配字符,包括换行符)"
url_list=re.findall('href=\"(.*?)\"',page,re.S)
url_all=[]
for url in url_list:
    if 'http' in url:
        print(url)
        url_all.append(url)
print(url_all)