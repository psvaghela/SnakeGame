from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

passw = "Vps@4104"
driver = webdriver.Chrome("F:\\down\\chromedriver_win32 (3)\\chromedriver.exe")

url = "https://www.instagram.com/"
driver.get(url)
time.sleep(5)

    
#try:
username = driver.find_element(By.XPATH,"//input[@name='username']")
username.send_keys("sweetweet.surat")
pword = driver.find_element(By.XPATH, "//input[@name='password']")
pword.send_keys(passw)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
#time.sleep(30)
driver.find_element(By.XPATH, "//a[@href='/?next=%2F']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='_a9-- _a9_1']").click()
#driver.quit()
driver.get("https://www.instagram.com/surat_foodie/followers/?next=%2F")
time.sleep(5)


fpath = "_acan" 
fbutton = driver.find_elements(By.CLASS_NAME,fpath)
time.sleep(2)
print(fbutton)
print(len(fbutton))

for i in fbutton:
    i.click()
    
'''except:
    #pword = driver.find_element(By.XPATH, "//input[@name='password']")
    #pword.send_keys('')
    url = "https://www.instagram.com/"
    driver.get(url)
    time.sleep(2)'''


    