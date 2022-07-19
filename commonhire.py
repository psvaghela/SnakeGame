import os
import tkinter
from tkinter import simpledialog
from datetime import date

dt = str(date.today())   # Today's date
dy = dt.replace(dt[-1],str(int(dt[-1])-1))  # yesterday date

###### Create New Directory in HR-DB #######
parent_dir = "E:\HR_DB"
pathd = os.path.join(parent_dir,dt)
os.mkdir(pathd)
'''dir_new = "New"
dir_final = "Final"
pathn = os.path.join(pathd,dir_new)
pathf = os.path.join(pathd,dir_final)
os.mkdir(pathn)
os.mkdir(pathf)'''

######## Define Function to Extract data ########
def hirelinkedin(techn,file_name):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import time
    import pandas as pd

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

    ### sign-in done on linkedin

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
    #recenturl = s.replace('?','?datePosted=%22past-week%22&') # Last week posts
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


    #file_new = "E:\\HR_DB\\" + dt + "\\New\\" + dt + "_" + file_name  # New File
    file_old = "E:\\HR_DB\\" + dy + "\\" + dy + "_" + file_name   ## Old File(yesterday's)
    file_final = "E:\\HR_DB\\" + dt + "\\" + dt + "_" + file_name   ## Final file containing unique elements.

    dic = {'Name':nam, 'Recent-activity Posts':lnk, 'Post Time':pt}
    df1 = pd.DataFrame(dic)
    df1.drop_duplicates(inplace=True)
    df2 = pd.read_csv(file_old)
    df3 = df1.merge(df2, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only'] # Taking Data which is in df1 but not in df2
    df3.to_csv(file_final, header=True, index=False)  # Final CSV
    #df1.to_csv(file_new, header=True, index=False)   # New CSV(24-hrs data)

    time.sleep(5)
    driver.close()

    return None
# Function will accept technology name and file name.


###### Make GUI to take input from the user #########
window = tkinter.Tk()
window.withdraw()

techs = simpledialog.askstring(title="Technologies List",prompt="Enter Technologies Separated by Comma:")
techl = techs.split(',')

####### Call finction for all technologies in the input #######
for x in techl:
    if('/' in x):
        x = x.replace('/','')
    hirelinkedin(x,x+'.csv')

print("Task Completed....")