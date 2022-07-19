from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Make interface for file selection
Tk().withdraw()
filename = askopenfilename()

ts = random.randint(10,30)
df = pd.read_csv(filename)
l = len(df)

driver = webdriver.Chrome("C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://web.whatsapp.com/"
driver.get(url)
print("Scan QR Code")
#scan qr code to login into whatsapp

time.sleep(30)
srchbox = driver.find_element(By.XPATH, "//div[@class='_13NKt copyable-text selectable-text']")  # Searchbox
srchbox.click()

for i in range(l):
    
    mob = str(df.at[i,'Mobile'])  # Mobile/Whatsapp Number
    nam = str(df.at[i,'Name'])    # Name
    mess = "Hello " + nam + ", Maja ma?"   # Message
    # Going to page of candidate in whatsapp
    srchbox.send_keys(mob)
    time.sleep(1)
    srchbox.send_keys(Keys.ENTER)
    
    p = driver.page_source
    soup= BeautifulSoup(p,'lxml')
    lastmess = soup.find_all('span',{'class':"i0jNr selectable-text copyable-text"},string=True)[-1]  # list of all messages
    recent = lastmess.get_text(strip=True)  # Last Message
    time.sleep(2)
    
    # If message already sent before, candidate will not get same message again.
    if(recent!=mess):
        messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
        messbox.send_keys(mess)
        messbox.send_keys(Keys.ENTER)  # Message sent with ENTER Key
        print("Message sent successfully!!!")
    else:
        continue
    
    time.sleep(ts)  # Stop for random time


print("Task Completed....")
#driver.close()  # Close the window