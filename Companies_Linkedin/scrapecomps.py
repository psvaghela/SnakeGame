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
#sign-in done in linkedin

#links list will store links of all company profiles
links = []
for i in range(1,101):
        search_url = "https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22114495808%22%5D&industry=%5B%2296%22%5D&origin=FACETED_SEARCH&page="
        driver.get(search_url+str(i))
        time.sleep(7)
        p = driver.page_source
        soup = BeautifulSoup(p,'lxml')
        comps = soup.find_all('div', {'class':"entity-result"})
        for comp in comps:
            link = comp.find('a',{'class':"app-aware-link"},href=True)
            d = link['href']
            links.append(d)
        print(len(links))
print(len(links))
#All company-page links will be saved in links list.
#we can iterate through all links to extract data.

time.sleep(10)
#all data will be stored in surat_comps.csv
with open('surat_comps.csv','w',encoding='utf8',newline='') as s:
    swriter = writer(s)
    header = ['Company Name','Contact Number','Company Website','Industry','Company Size','Company Headquarters Location','Linkedin Followers','Description']
    swriter.writerow(header)

    for link in links:
        comp_url = str(link)+"about/"
        if(comp_url == "https://www.linkedin.com/company/s3-info-services-pvt-ltd/about/"):
            continue
        driver.get(comp_url)
        time.sleep(5)
        ss = driver.page_source
        soup = BeautifulSoup(ss,'lxml')
        #print(soup.prettify())

        #Introduction Section:
        intro = soup.find('div',{'class':"ph5 pt3"})
        dep = soup.find('dl',{'class':"overflow-hidden"})
        if(intro != None):
            inn1 =  intro.find_all('div',{'class':"org-top-card-summary-info-list__info-item"},string=True)
        else:
            inn1 = []
        
        if(dep != None):
            inn2 = dep.find_all('span',{'class':"link-without-visited-state"},string=True)
        else:
            inn2 = []
        
        #Company Name and Description:
        if(intro != None):
            name = intro.find('span')
            if(name != None):
                names = name.get_text(strip=True)
            else:
                names = " "

            desc = intro.find('p',{'class':"org-top-card-summary__tagline"})
            if(desc != None):
                description = desc.get_text(strip=True)
            else:
                description = " "
        else:
            names = " "
            description = " "

        #Industry:
        if(len(inn1)>=1):
            indus = inn1[0]
            if(indus != None):
                industry = indus.get_text(strip=True)
            else:
                industry = " "
        else:
            industry = " "

        #Headquarters Location:
        if(len(inn1)>=2):
            loc = inn1[1]
            if(loc != None):
                location = loc.get_text(strip=True)
            else:
                location = " "
        else:
            location =" "

        #Number of Followers on Linkedin
        if(len(inn1)>=3):
            follow = inn1[2]
            if(follow != None):
                followers = follow.get_text(strip=True)
            else:
                followers = " "
        else:
            followers = " "
        
        #Company Website:
        if(len(inn2)>=1):
            webs =inn2[0]
            if(webs != None):
                website = webs.get_text(strip=True)
            else:
                website = " "
        else:
            website = " "

        #Company size(No. of Employees):
        if(dep != None):
            siz = dep.find('dd',{'class':"text-body-small t-black--light mb1"})
            if(siz != None):
                size = siz.get_text(strip=True)
            else:
                size = " "
        else:
            size = " "

        #Company Contact Number:
        if(len(inn2)>=2):
            contact = inn2[1]
            if(contact != None):
                contact_no = contact.get_text(strip=True)
            else:
                contact_no = " "
        else:
            contact_no = " "

        #Save all Data into surat_comps.csv
        info = [names,contact_no,website,industry,size,location,followers,description]
        swriter.writerow(info)
        #print(names,contact_no,website,industry,size,location,followers,description)

time.sleep(10)
#close the window
driver.close()
#If window closed, Program completed Successfully!!