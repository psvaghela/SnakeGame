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

# sign-in done on linkedin
#opening csv file to save data
#writer will write data into surat.csv
with open('surat.csv','w',encoding='utf8',newline='') as s:
    swriter = writer(s)
    header = ['Company Name','Headquarters Location','Followers','Job Openings','Description']
    swriter.writerow(header)
    
    #Iterating through 100 pages of different links to extract data.
    for i in range(1,101):
        search_url = "https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22114495808%22%5D&industry=%5B%2296%22%5D&origin=FACETED_SEARCH&page="
        driver.get(search_url+str(i))
        time.sleep(7)
        p = driver.page_source
        soup = BeautifulSoup(p,'lxml')
        #print(soup.prettify())

        #comps will save all company cards.
        comps = soup.find_all('div', {'class':"entity-result"})
        #print(comps)
    
        for comp in comps:
            #print(comp)
            name = comp.find('span', {'class':"entity-result__title-text t-16"}).get_text(strip=True)
            location = comp.find('div', {'class':"entity-result__primary-subtitle t-14 t-black t-normal"}).get_text(strip=True).replace("IT Services and IT Consulting • ","")
            followers = comp.find('div', {'class':"entity-result__secondary-subtitle t-14 t-normal"}).get_text(strip=True)
            job = comp.find('span', {'class':"entity-result__simple-insight-text"})
            if(job != None):
                jobs = job.get_text(strip=True)
            else:
                jobs = " "
            #If job is available, It will be stored in csv file.
            description = comp.find('p', {'class':"entity-result__summary"})
            if(description != None):
                desc = description.get_text(strip=True)
            else:
                desc = " "
            #If description is given by company, It will be stored in csv file.
            #print(name,location,followers,jobs,description)
            info = [name,location,followers,jobs,desc]
            swriter.writerow(info)
            
#close the window
driver.close()
#If window closed, Program Successful!!