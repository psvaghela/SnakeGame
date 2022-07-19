from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import tkinter
from tkinter import simpledialog

window = tkinter.Tk()
window.withdraw()

kword = simpledialog.askstring(title="Key-Word",prompt="Enter key word to extract data")
file_name = simpledialog.askstring(title="File-Name",prompt="Enter file name to save data")

driver = webdriver.Chrome("C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://linkedin.com/uas/login"
driver.get(url)
time.sleep(5)
username = driver.find_element(By.ID, "username")
username.send_keys("hrj3285@gmail.com")
pword = driver.find_element(By.ID, "password")
pword.send_keys("Hrj@1234")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)

# sign-in done on linkedin

nam = []
lnk = []
pt = []

#kword = "looking for job in " + tech_name
srchbox = driver.find_element(By.XPATH, "//input[@type='text']")
srchbox.send_keys(kword)
srchbox.send_keys(Keys.ENTER)
time.sleep(4)

postbutton = driver.find_element(By.XPATH, "//button[text()='Posts']")
postbutton.click()
time.sleep(5)

# For Past 24-hours posts:

s = driver.current_url
recenturl = s.replace('?','?datePosted=%22past-week%22&') # Recent Activity URL
driver.get(recenturl)
time.sleep(5)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    p = driver.page_source
    soup = BeautifulSoup(p,'lxml')
    profs = soup.find_all('div', {'class':"feed-shared-actor"})

    for prof in profs:
        name = prof.find('span',{'dir':"ltr"})
        if(name!=None):
            names = name.get_text(strip=True)
        else:
            continue
        prof_url = prof.find('a',{'class':"app-aware-link feed-shared-actor__container-link relative display-flex flex-grow-1"},href=True)
        posttime = prof.find_all('span',{'class':"visually-hidden"})[-1]
        if(posttime!=None):
            postt = posttime.get_text(strip = True)
        else:
            continue
        pt.append(postt)
        l = prof_url['href']
        nam.append(names)
        newl = l.split('?')[0] + '/recent-activity/'
        lnk.append(newl)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(7)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


file_n = "C:\\Users\\Dell\\Downloads\\" + file_name + ".csv"   # Save file name

dic = {'Name':nam, 'Recent-activity Posts':lnk, 'Post Time':pt}
df = pd.DataFrame(dic)
df.drop_duplicates(inplace=True)
df.to_csv(file_n,header=True,index=False)

time.sleep(5)
driver.close()