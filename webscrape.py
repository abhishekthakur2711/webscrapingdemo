# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:17:29 2019

@author: abhishekthakur
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time

#Initializing the Webdriver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chrome_options)

#Opening the Website to crawl
driver.get("https://www.flipkart.com/")

#defining credentials
usernameStr = '9900952361'
passwordStr = '124500'
#defining object to scrape for - can be a list and looped for multiple object
searchStr = 'Power Banks'

#logging into the website
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys(usernameStr)

driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').send_keys(passwordStr)

driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button').click()

time.sleep(3)

#searching for our product list
search_box = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search_box.send_keys(searchStr)
search_box.send_keys(Keys.ENTER)

time.sleep(3)

#extracting the attributes - notice the element"s"
products = driver.find_elements_by_tag_name('a')


#for product in products:
#    print(product)

#extracting product titles in a list
titles=[]

for product in products:
    titles.append(product.get_attribute('title'))
    
driver.quit()

#filtering for relevant results    
parenthesis = re.compile('.*\)')
bank = re.compile('.*Bank')
temp = list(filter(parenthesis.match, titles))
powerbanks = list(filter(bank.match, temp))  # Read Note

#display results
for product in powerbanks:
    print(product)
