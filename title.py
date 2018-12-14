from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
time.sleep(2)
#获取标题
title=driver.title
print(title)
time.sleep(2)
#获取元素文本
text=driver.find_element_by_id('setf').text
time.sleep(2)
print(text)
#获取标签
tag=driver.find_element_by_id('kw').tag_name
print(tag)
#获取输入框class属性
s=driver.find_element_by_id('kw').get_attribute('class')
print(s)
driver.find_element_by_id('kw').send_keys(u'你好')
time.sleep(2)
#获取输入框value信息
p=driver.find_element_by_id('kw').get_attribute('value')
print(p)
#获取浏览器信息
print(driver.name)