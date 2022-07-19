from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://linkedin.com/uas/login"
driver.get(url)
time.sleep(5)
username = driver.find_element_by_id("username")
username.send_keys("hrj3285@gmail.com")
pword = driver.find_element_by_id("password")
pword.send_keys("Hrj@1234")

driver.find_element_by_xpath("//button[@type='submit']").click()

search_url = "https://www.linkedin.com/search/results/content/?keywords=halol&origin=SWITCH_SEARCH_VERTICAL&position=0&searchId=901cc81e-31fe-43ea-82db-315371fdedf8&sid=EE-"
driver.get(search_url)
time.sleep(5)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(5)
driver.close()