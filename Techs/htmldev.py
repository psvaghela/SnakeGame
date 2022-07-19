from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

nm = []
psn = []
dt = []

driver = webdriver.Chrome("C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://linkedin.com/uas/login"
driver.get(url)
time.sleep(5)
username = driver.find_element_by_id("username")
username.send_keys("hrj3285@gmail.com")
pword = driver.find_element_by_id("password")
pword.send_keys("Hrj@1234")
driver.find_element_by_xpath("//button[@type='submit']").click()

# sign-in done on linkedin

search_url = "https://www.linkedin.com/search/results/content/?keywords=hiring%20html%20developer&origin=GLOBAL_SEARCH_HEADER&sid=54r"
driver.get(search_url)
time.sleep(5)

i=0
while i<100:
    g = driver.page_source
    soup = BeautifulSoup(g, 'lxml')
    boxes = soup.find_all("div", {'class': "ember-view"})

    for box in boxes:
        # Name of the Writer
        name = box.find('span', {'class': "feed-shared-actor__name"})
        if(name != None):
            names = name.get_text(strip=True)
        else:
            continue

        # Position of Writer/Description
        position = box.find('span', {'class': "feed-shared-actor__description"})
        if(position != None):
            positions = position.get_text(strip=True)
        else:
            continue

        # Data that is written in post
        data = box.find('span', {'class': "break-words"})
        if(data != None):
            datas = data.get_text(strip=True)
        else:
            continue
        nm.append(names)
        psn.append(positions)
        dt.append(datas)
        

    # Scrolling Down by 8000 pixels in each loop.
    driver.execute_script("window.scrollBy(0,10000)", "")
    time.sleep(5)
    i = i+1

driver.close()

dic1 = {'Name':nm,'Position':psn,'Data':dt}
df = pd.DataFrame(dic1)
df.drop_duplicates(inplace=True)
df.to_csv("html.csv",header=True,index=False)
