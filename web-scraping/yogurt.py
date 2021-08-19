# import libraries
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
# specify the url
urlpage = 'https://groceries.asda.com/search/yogurt'  #'https://vadmvappointments.as.me/schedule.php' 
print(urlpage)
# query the website and return the html to the variable 'page'
#page = requests.get(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
#soup = BeautifulSoup(page.content, 'html.parser')
# find product items
# at time of publication, Nov 2018:
# results = soup.find_all('div', attrs={'class': 'listing category_templates clearfix productListing'})
# updated Nov 2019:
#results = soup.find_all('div', attrs={'class': 'step-container'})
#print('Number of results', len(results))

# run firefox webdriver from executable path of your choice
driver = webdriver.Firefox()
# get web page
driver.get(urlpage)
time.sleep(30)
results = driver.find_elements_by_xpath("//*[@class=' co-product-list__main-cntr']//*[@class=' co-item ']//*[@class='co-product']//*[@class='co-item__title-container']//*[@class='co-product__title']")
print('Number of results', len(results))

# create empty array to store data
data = []
# loop over results
for result in results:
    product_name = result.text
    link = result.find_element_by_tag_name('a')
    product_link = link.get_attribute("href")
    # append dict to array
    data.append({"product" : product_name, "link" : product_link})

# close driver 
driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)