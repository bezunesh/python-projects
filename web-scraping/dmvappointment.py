# import libraries
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
# stafford - 874 Garisonville Road
urlpage =  'https://vadmvappointments.as.me/schedule.php?calendarID=5776807'
print(urlpage)

driver = webdriver.Firefox()
# get web page
driver.get(urlpage)
time.sleep(30)

results = driver.find_elements_by_xpath("//*[@class='calendar']//*[@class='calendar-date-row']//*[@class='scheduleday  activeday']")
print('Number of results', len(results))

if(len(results) >= 1):
    # send notification
    print("Available dates: ")
    # loop over results
    for result in results:
        calendar_date = result.get_attribute("day")
        print(calendar_date)
