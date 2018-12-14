from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('file:///C:/Users/Administrator/Desktop/alert.html')
driver.implicitly_wait(30)
driver.maximize_window()
time.sleep(2)
# alert操作
driver.find_element_by_id('alert').click()
time.sleep(2)
t=driver.switch_to.alert
time.sleep(2)
print(t.text)
t.dismiss()
time.sleep(2)

# #confirm操作
# driver.find_element_by_id('confirm').click()
# time.sleep(2)
# driver.switch_to.alert.accept()
# time.sleep(2)
# driver.find_element_by_id('confirm').click()
# time.sleep(2)
# driver.switch_to.alert.dismiss()
# time.sleep(2)

# #prompt操作
# driver.find_element_by_id('prompt').click()
# time.sleep(2)
# driver.switch_to.alert.send_keys(u'你好，python')
# time.sleep(2)
# driver.switch_to.alert.accept()
# time.sleep(2)
# driver.quit()