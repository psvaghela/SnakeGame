from selenium import webdriver
import time
import tkinter
from tkinter import simpledialog

window = tkinter.Tk()
window.withdraw()

user_id = simpledialog.askstring(title="E-Mail",prompt="Enter your E-Mail")
password = simpledialog.askstring(title="Password",prompt="Enter Password")

driver = webdriver.Chrome("C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://linkedin.com/uas/login"
driver.get(url)
time.sleep(5)
username = driver.find_element_by_id("username")
username.send_keys(user_id)
pword = driver.find_element_by_id("password")
pword.send_keys(password)
driver.find_element_by_xpath("//button[@type='submit']").click()
#sign-in done in linkedin

