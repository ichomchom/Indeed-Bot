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

# Click on job search with recent search
driver.find_element_by_xpath('//*[@id="hp-job-search"]').click()

# Wait 10s for page to load
driver.implicitly_wait(10)

# Create jobs list
jobs = driver.find_elements_by_class_name('summary')

# Main window
main = driver.window_handles[0]

for job in jobs:

    # Click on each job
    job.click()

    driver.implicitly_wait(20)

    # Click on apply job
    driver.find_element_by_xpath('//*[@id="PrimaryJobApply"]').click()
        
    # If open new page, go to that page and close the page
    if len(driver.window_handles) == 2:
        driver.switch_to_window(driver.window_handles[1])
        driver.close()
        driver.switch_to_window(main)

        #elif driver.find_element_by_xpath('//*[@id="SpeedApply"]/section/div/div[2]/a').is_enabled():
            #continue

    # Apply using monster only click apply
    else:
        driver.find_element_by_xpath('//*[@id="applybtn"]').click()
           
        # TODO: Fix when go back to main page go to next job

        # If job already applied, alert pop up, then go back to main page
        if driver.find_element_by_xpath('//*[@id="ApplyAlert"]').is_enabled():
            driver.back()
            driver.back()
            
        driver.find_element_by_xpath('//*[@id="ListSwitch"]/i').click()