# import libraries
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import notify

def getAppointmentDates():
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
    
    return available_dates

if __name__ == '__main__':
    available_dates = getAppointmentDates()
    if available_dates is not None:
       notify.sendEmail(available_dates)