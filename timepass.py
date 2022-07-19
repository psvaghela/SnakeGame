from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

nn = "PSV"    # Name/Number
#mess1 = "Pithva"
#mess2 = "mc"
#mess3 = "Bc"
#mess4 = "lawde"
#mess5 = "ghant"  # Message

driver = webdriver.Chrome("C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://web.whatsapp.com/"
driver.get(url)
print("Scan QR Code")

time.sleep(30)
srchbox = driver.find_element(By.XPATH, "//div[@class='_13NKt copyable-text selectable-text']")
srchbox.click()

srchbox.send_keys(nn)
time.sleep(2)
srchbox.send_keys(Keys.ENTER)

for i in range(100):
    #time.sleep(10)
    #messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
    #messbox.send_keys(mess1)
    #messbox.send_keys(Keys.ENTER)

    '''#time.sleep(1)
    messbox.send_keys(mess2)
    messbox.send_keys(Keys.ENTER)
    #time.sleep(1)
    messbox.send_keys(mess3)
    messbox.send_keys(Keys.ENTER)
    #time.sleep(1)
    messbox.send_keys(mess4)
    messbox.send_keys(Keys.ENTER)
    #time.sleep(1)
    messbox.send_keys(mess5)
    messbox.send_keys(Keys.ENTER)
    #time.sleep(1)
    #print("Message sent successfully!!!")'''

    emobox = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[2]")
    emobox.click()
    time.sleep(2)
    stkbox = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[4]")
    stkbox.click()
    time.sleep(2)
    stk = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[2]/div/div[3]/div/div/div[2]/div[2]/div/div/div/div[3]/div")
    stk.click()

#time.sleep()
print("Task Completed....")