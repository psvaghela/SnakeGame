from selenium import webdriver
from bs4 import BeautifulSoup
import time
from csv import writer

driver = webdriver.Chrome("C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://linkedin.com/uas/login"
driver.get(url)
time.sleep(5)
username = driver.find_element_by_id("username")
username.send_keys("hrj3285@gmail.com")
pword = driver.find_element_by_id("password")
pword.send_keys("Hrj@1234")
driver.find_element_by_xpath("//button[@type='submit']").click()

links = []
for i in range(1,101):
        search_url = "https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22114495808%22%5D&industry=%5B%2296%22%5D&origin=FACETED_SEARCH&page="
        driver.get(search_url+str(i))
        time.sleep(2)
        p = driver.page_source
        soup = BeautifulSoup(p,'lxml')
        comps = soup.find_all('div', {'class':"entity-result"})
        for comp in comps:
            link = comp.find('a',{'class':"app-aware-link"},href=True)
            d = link['href']
            links.append(d)
print(len(links))
print(links)

driver.close()
