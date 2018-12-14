'--user-data-dir=C:\Users\username\AppData\Local\Google\Chrome\User Data'
from selenium import webdriver
option=webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:\Users\Gloria\AppData\Local\Google\Chrome\User Data')
driver = webdriver.Chrome(chrome_options=option)
driver.implicitly_wait(30)
driver.get("http://www.cnblogs.com/yoyoketang/")
