# import libraries
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import notify
import schedule

def getAppointmentDates():
    # Stafford  Garsionville DMV
    #urlpage =  'https://vadmvappointments.as.me/schedule.php?calendarID=5101548'
    urlpage = 'https://vadmvappointments.as.me/schedule.php?calendarID=5101548'
    print(urlpage)

    driver = webdriver.Firefox()
    # get web page
    driver.get(urlpage)
    time.sleep(5)

    results = driver.find_elements_by_xpath("//*[@class='calendar']//*[@class='scheduleday  activeday']")
    print('Number of results', len(results))

    available_dates = []
    if(len(results) >= 1):
        for result in results:
            calendar_date = result.get_attribute("day")
            available_dates.append(calendar_date)
    
    if available_dates:
        notify.sendEmail(available_dates)
    

if __name__ == '__main__':
    schedule.every(10).minutes.do(getAppointmentDates)
 
    while True:
        schedule.run_pending()