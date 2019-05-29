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
driver.get('https://www.linkedin.com/')

driver.find_element_by_xpath('/html/body/nav/a[3]').click()

# Log in
driver.find_element_by_xpath('//*[@id="username"]').send_keys(info.email)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(info.password)
driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button').click()

# Go to Jobs
driver.find_element_by_xpath('//*[@id="jobs-nav-item"]/a').click()


# Fill out job title and location
driver.find_element_by_xpath('//*[@id="ember611"]/span[1]').click()

# Wait 10s for page to load
driver.implicitly_wait(10)

# Create jobs list


# Main window
main = driver.window_handles[0]

for job in jobs:
    try:
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

            # If job already applied, alert pop up, then go back to main page
            if driver.find_element_by_xpath('//*[@id="ApplyAlert"]').is_enabled():
                driver.back()
                driver.back()
                continue
    except Exception as er:
        print(er)
