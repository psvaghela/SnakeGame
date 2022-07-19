from selenium import webdriver
from bs4 import BeautifulSoup
import time
from csv import writer
import pandas as pd

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

search_url = "https://www.linkedin.com/search/results/content/?keywords=Need%20a%20WordPress%20developer%20&origin=GLOBAL_SEARCH_HEADER&sid=q-s"
driver.get(search_url)
time.sleep(5)

# print(soup.prettify())
with open('wordpress.csv', 'w', encoding='utf8', newline='') as x:
    xwriter = writer(x)
    header = ['Name of Writer', 'Position of Writer', 'Data']
    xwriter.writerow(header)
    i = 0
    while i < 50:
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
            position = box.find(
                'span', {'class': "feed-shared-actor__description"})
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

            info = [names, positions, datas]
            xwriter.writerow(info)

        # Scrolling Down by 8000 pixels in each loop.
        driver.execute_script("window.scrollBy(0,8000)", "")
        time.sleep(5)
        i = i+1

# Close Window
driver.close()

# Converting csv file to pandas dataframe to remove duplicate rows.
asp = pd.read_csv('wordpress.csv')
asp.drop_duplicates(inplace=True)
asp.to_csv('new_wordpress.csv', index=False)
