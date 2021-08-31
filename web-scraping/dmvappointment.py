# import libraries
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import smtplib

def checkAppointment():
    urlpage =  'https://vadmvappointments.as.me/schedule.php?calendarID=5776807'
    print(urlpage)

    driver = webdriver.Firefox()
    # get web page
    driver.get(urlpage)
    time.sleep(15)

    results = driver.find_elements_by_xpath("//*[@class='calendar']//*[@class='scheduleday  activeday']")
    print('Number of results', len(results))

    available_dates = []
    if(len(results) >= 1):
        for result in results:
            calendar_date = result.get_attribute("day")
            available_dates.append(calendar_date)
        
        email_text = "Available dates are: \n" + ', '.join(available_dates)
        print(email_text)

if __name__ == '__main__':
    checkAppointment()