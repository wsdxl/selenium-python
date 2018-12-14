from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('file:///C:/Users/Administrator/Desktop/box.html')
time.sleep(2)
driver.maximize_window()
time.sleep(2)
# # 勾选单选框
# driver.find_element_by_id('boy').click()
# time.sleep(10)
# driver.find_element_by_id('girl').click()

#勾选复选框
# driver.find_element_by_id('c1').click()
# time.sleep(2)

# #全选复选框
# checkboxs=driver.find_elements_by_xpath("//form/input[@type='checkbox']")
# for i in checkboxs:
#     i.click()

#判断按钮是否选中
s=driver.find_element_by_id('boy').is_selected()
print(s)
driver.find_element_by_id('boy').click()
time.sleep(2)
t=driver.find_element_by_id('boy').is_selected()
print(t)