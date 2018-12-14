#coding:utf-8
from selenium import webdriver
option=webdriver.ChromeOptions()
#伪装iphone登录
option.add_argument('--user-agent=iphone')
#伪装android登录
# option.add_argument('--user-agent=android')
driver=webdriver.Chrome(chrome_options=option)
driver.get('http://www.taobao.com')