from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://www.instagram.com/"
driver.get(url)

time.sleep(5)
username = driver.find_element(By.XPATH,"//input[@name='username']")
username.send_keys("discbiz")
pword = driver.find_element(By.XPATH, "//input[@name='password']")
pword.send_keys("Vps@4104")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(20)
#time.sleep(30)
driver.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a/svg").click()
time.sleep(10)
driver.quit()