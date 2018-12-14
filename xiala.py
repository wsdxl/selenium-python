# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.implicitly_wait(30)
driver.maximize_window()
#鼠标移动到设置按钮
mouse=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text('搜索设置').click()
time.sleep(3)
# #直接根据xpath定位
# driver.find_element_by_xpath('//select[@id="nr"]/option[2]').click()

# #通过索引：select_by_index()
# s=driver.find_element_by_id('nr')
# time.sleep(3)
# Select(s).select_by_index(1)

# #通过value：select_by_value()
# s=driver.find_element_by_id('nr')
# time.sleep(2)
# Select(s).select_by_value('20')

#通过text:select_by_visible_text
s=driver.find_element_by_id('nr')
time.sleep(2)
Select(s).select_by_visible_text('每页显示50条')
time.sleep(2)
s.click()
driver.find_element_by_link_text('保存设置').click()
time.sleep(2)
s=driver.switch_to.alert
print(s.text)
s.accept()
time.sleep(2)