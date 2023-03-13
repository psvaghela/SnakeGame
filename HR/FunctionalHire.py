from datetime import date
from datetime import timedelta
from selenium import webdriver

today = date.today()
dt = str(today)   # Today's date
yest = today - timedelta(days=1)  # yesterday's date
dy = str(yest)

driver = webdriver.Chrome("C:\\Users\\Dell\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe")
    #"C:\Users\Dell\Downloads\chromedriver_win32 (1)\chromedriver.exe"

def makefolder():
    """Makes The Folder in Local Computer"""
    import os

    try:
        parent_dir = "E:\\HR_DB"
        pathd = os.path.join(parent_dir,dt)
        os.mkdir(pathd)
        dir_new = "New"
        dir_final = "Final"
        pathn = os.path.join(pathd,dir_new)
        pathf = os.path.join(pathd,dir_final)
        os.mkdir(pathn)
        os.mkdir(pathf)
    except:
        pass


def login():
    """Login into Linkedin"""
    import time
    from selenium.webdriver.common.by import By

    url = "https://www.linkedin.com/login"
    driver.get(url)
    time.sleep(5)
    username = driver.find_element(By.ID, "username")
    username.send_keys("hrj3285@gmail.com")
    pword = driver.find_element(By.ID, "password")
    pword.send_keys("Hrj@1234")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)


def extract(techn,p):
    """Extracts Data:
    techn is list of technologies,
    p=0 for single day data,
    p=1 for last one week data"""
    import time
    from bs4 import BeautifulSoup
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import pandas as pd

    kword = "looking for job in " + techn   # Search keyword
    nam = []
    lnk = []
    pt = []
    
    srchbox = driver.find_element(By.XPATH, "//input[@type='text']")
    srchbox.send_keys(kword)
    srchbox.send_keys(Keys.ENTER)
    time.sleep(4)

    postbutton = driver.find_element(By.XPATH, "//button[text()='Posts']")
    postbutton.click()
    time.sleep(5)

    # For Past 24-hours posts:

    s = driver.current_url
    if p==1:
        recenturl = s.replace('?','?datePosted=%22past-week%22&') # Last week posts
        driver.get(recenturl)
    if p==0:
        recenturl = s.replace('?','?datePosted=%22past-24h%22&')
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
        time.sleep(5)
        driver.quit()

    file_name = techn + '.csv'
    file_new = "E:\\HR_DB\\" + dt + "\\New\\" + dt + "_" + file_name  # New File
    file_old = "E:\\HR_DB\\" + dy + "\\New\\" + dy + "_" + file_name   ## Old File(yesterday's)
    file_final = "E:\\HR_DB\\" + dt + "\\Final\\" + dt + "_" + file_name   ## Final file containing unique elements.

    dic = {'Name':nam, 'Recent-activity Posts':lnk, 'Post Time':pt}
    df1 = pd.DataFrame(dic)
    df1.drop_duplicates(inplace=True)
    try:
        df2 = pd.read_csv(file_old)
        df3 = df1.merge(df2, how = 'left' ,indicator=True)  #.loc[lambda x : x['_merge']=='left_only'] # Taking Data which is in df1 but not in df2
        df3.to_csv(file_final, header=True, index=False)  # Final CSV
        df1.to_csv(file_new, header=True, index=False)   # New CSV(24-hrs data)
    except FileNotFoundError:
        df1.to_csv(file_final, header=True, index=False)   # New CSV(24-hrs data)
        df1.to_csv(file_new, header=True, index=False)   # New CSV(24-hrs data)


def input():
    import tkinter
    from tkinter import simpledialog

    window = tkinter.Tk()
    window.withdraw()
    tdef = "laravel,wordpress,magento,node,flutter,MERN,react,UIUX,web designing,android,ios,SEO,digital marketing"
    techs = simpledialog.askstring(title="Technologies List",prompt="Enter Technologies Separated by Comma:")
    if techs=='' or techs ==0:
        techs = tdef
    tech1 = str(techs).split(',')
    return tech1

techdata = input()
makefolder()
login()
for i in techdata:
    extract(i,1)