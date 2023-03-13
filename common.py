def tech_data(kw,file_name):
    import time
    from datetime import date

    import pandas as pd
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    dt = str(date.today())   # Today's date
    dy = dt.replace(dt[-1],str(int(dt[-1])-1))  # yesterday date

    nm = []
    psn = []
    dt = []

    # Assign Different Paths for Files
    #path_old = "E:\\TECH_DB\\" + "2022-07-18" + "\\" + file_name  # Yesterday
    path_file = "E:\\TECH_DB\\" + "2022-07-21" + "\\" + file_name  # New posts that are increased Today than yesterday
    
    driver = webdriver.Chrome("C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe")
    url = "https://linkedin.com/uas/login"
    driver.get(url)
    time.sleep(5)
    username = driver.find_element(By.ID, "username")
    username.send_keys("hrj3285@gmail.com")
    pword = driver.find_element(By.ID, "password")
    pword.send_keys("Hrj@1234")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # sign-in done on linkedin

    kword = kw
    srchbox = driver.find_element(By.XPATH, "//input[@type='text']")
    srchbox.send_keys(kword)
    srchbox.send_keys(Keys.ENTER)
    time.sleep(4)

    postbutton = driver.find_element(By.XPATH, "//button[text()='Posts']")
    postbutton.click()
    time.sleep(5)
    s = driver.current_url
    #recenturl = s.replace('?','?datePosted=%22past-week%22&') # Last week posts
    recenturl = s.replace('?','?datePosted=%22past-24h%22&')  #24-hours
    driver.get(recenturl)
    time.sleep(5)
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    i=0
    while True:
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
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(10)
    driver.quit()
    
    dic1 = {'Name':nm,'Position':psn,'Data':dt}
    df1 = pd.DataFrame(dic1)
    df1.drop_duplicates(inplace=True)
    #df2 = pd.read_csv(path_old)  # Old Dataset(Already Available)
    # df1 represents new file
    # df2 represents old file
    #df3 = df1.merge(df2, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only'] # Taking Data which is in df1 but not in df2
    df1.to_csv(path_file,index=False) # Final Dataset
    #df1.to_csv(path_file,index=False) # New Dataset
    
    return None

#Calling Function for all Technologies:

'''tech_data("hiring angular developer","angular.csv")
tech_data("hiring c++ developer","c++.csv")
tech_data("hiring flutter developer","flutter.csv")
tech_data("hiring html developer","html.csv")
tech_data("hiring java developer","java.csv")
tech_data("hiring javascript developer","javascript.csv")'''
tech_data("hiring laravel developer","laravel.csv")
tech_data("hiring node developer","node.csv")
tech_data("hiring python developer","python.csv")
tech_data("hiring react developer","react.csv")
tech_data("hiring sql developer","sql.csv")
tech_data("hiring wordpress developer","wordpress.csv")

# Save count of rows in each csv file
from datetime import date
import pandas as pd

# First column date
date_today = str(date.today())
list1 = [date_today]

postcount = pd.DataFrame(columns=['Date','Angular','C++','Flutter','HTML','Java','JavaScript','Laravel','node','Python','React','SQL','WordPress'])
files_list = ['angular.csv','c++.csv','flutter.csv','html.csv','java.csv','javascript.csv','laravel.csv','node.csv','python.csv', 
'react.csv','sql.csv','wordpress.csv']

for file_name in files_list:
    path_count = "E:\\TECH_DB\\2022-07-21\\" + file_name
    df = pd.read_csv(path_count)
    l = len(df)
    list1.append(l)

# Appending list data to pamndas DataFrame
postcount.loc[len(postcount)] = list1
postcount.to_csv("E:\\TECH_DB\\trend.csv", mode='a', index=False, header=False)
# Saved count of rows into count.csv file
