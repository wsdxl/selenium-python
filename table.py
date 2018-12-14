from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('file:///C:/Users/Administrator/Desktop/table.html')
driver.maximize_window()
time.sleep(2)
s=driver.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[2]/td[1]')
print(s.text)