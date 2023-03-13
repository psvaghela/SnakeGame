from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Dell\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
#"C:\Users\Dell\Downloads\chromedriver_win32 (1)\chromedriver.exe"
url = "http://172.50.1.1:8090/"
driver.get(url)
time.sleep(1)

username = driver.find_element(By.ID, "username")
username.send_keys("U20ME086")
pword = driver.find_element(By.ID, "password")
pword.send_keys("Svnit@15042003")
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='loginbutton']").click()