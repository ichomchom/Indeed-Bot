from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup

import info

# Create chrome driver
driver = webdriver.Chrome()

# Headless chrome driver
#options.headless = True

# Open the driver and go to monster.com
driver.get('https://login20.monster.com')

# Log in
driver.find_element_by_xpath('//*[@id="EmailAddress"]').send_keys(info.email)
driver.find_element_by_xpath('//*[@id="Password"]').send_keys(info.password)
driver.find_element_by_xpath('//*[@id="btn-login"]').click()

"""
# Fill out job title
titleElem = driver.find_element_by_xpath('//*[@id="rs-search-job"]"]')
titleElem.send_keys(Keys.CONTROL, 'a')
titleElem.send_keys(info.title)
whereElem = driver.find_element_by_xpath('//*[@id="rs-search-location"]')
whereElem.send_keys(Keys.CONTROL, 'a')
whereElem.send_keys(info.zipCode)
whereElem.submit()
"""
driver.find_element_by_xpath('//*[@id="hp-job-search"]').click()

driver.implicitly_wait(10)
jobs = driver.find_elements_by_class_name('summary')

# Main window
main = driver.window_handles[0]
for job in jobs:
    job.click()
    driver.find_element_by_xpath('//*[@id="PrimaryJobApply"]').click()
    applyButton = driver.find_element_by_xpath('//*[@id="applybtn"]')
    if applyButton.is_displayed:
        applyButton.click()
    else:
        tab = driver.window_handles[1]
        driver.switch_to_window(tab)
        driver.close()
        driver.switch_to_window(main)