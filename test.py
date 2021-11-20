
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
PATH ="E:/python downloads/chromedriver.exe"
driver = webdriver.Chrome(PATH)
import pywhatkit as kit
import time

list=['love nwatiti','alcohol','knife talk']
for song in list:
    
    url='https://www.youtube.com/results?search_query='+song
    driver.execute_script(f"window.open('{url}');")
    time.sleep(20)
    meta=driver.find_element_by_id('meta')
    meta.click()
    driver.execute_script(f"window.open('{url}');")
    time.sleep(5)
    driver.close()
    time.sleep(50)

#driver.execute_script("window.open('');")