from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup

import info

# Open Cover Letter
cv = open('./cv.txt', 'r')

# Read the content
content = cv.read()

# Create chrome driver
driver = webdriver.Chrome()

# Headless chrome driver
#options.headless = True

# Open the driver and go to angel.co
driver.get('https://angel.co/')

# Find the log in button
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/a[2]').click()

# Fill out email and password for login
driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(info.email)
driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(info.password)
driver.find_element_by_xpath('//*[@id="new_user"]/div[2]/input').click()


driver.implicitly_wait(10)

#html = driver.page_source

#soup = BeautifulSoup(html)
#jobs = soup.find_all('data-startup_ids')

while True:
    # Find the blue button to apply
    driver.find_element_by_xpath('//*[@id="startups_content"]/div[1]/div[5]/div/div/div[2]/div[2]/table/tbody/tr/td[2]/div/div[2]/a[1]').click()

    # Switch to popup frame
    #driver.switch_to.frame

    # Find the xpath for the apply button
    #apply = driver.find_element_by_xpath('//*[@id="layouts-base-body"]/div[12]/div/div/div/div/div/div[1]/div/div[2]/button')

    # Fill out Cover Letter
    note = driver.find_element_by_xpath('//*[@id="layouts-base-body"]/div[13]/div/div/div/div/div/div[1]/div/textarea')
    companyName = driver.find_element_by_class_name('startup-title').text[9::]
    position = driver.find_element_by_class_name('job-title').text
    
    note.send_keys(content % (position, companyName, info.phone, info.email, info.name))
    # Check if the apply button available or not
    # if apply.is_enabled:
    #     apply.click()
    #     driver.implicitly_wait(10)
    # else:
    #     # If not available click cancel
    #     driver.find_element_by_xpath('//*[@id="layouts-base-body"]/div[12]/div/div/div/div/div/div[1]/div/div[2]/button').click()

    # Close the popup frame
    #driver.find_element_by_xpath('//*[@id="layouts-base-body"]/div[12]/div/div/div/div/div/div[2]/div/div[3]/button').click()

    # Refresh browser to reapply the job
    #driver.refresh()

# TODO: Find all jobs to open and apply instead of refresh
"""
//*[@id="startups_content"]/div[1]/div[5]/div/div/div[2] # 1st job
//*[@id="startups_content"]/div[1]/div[5]/div/div/div[3] # 2nd job 
//*[@id="startups_content"]/div[1]/div[5]/div/div/div[2]/div[2]/table/tbody/tr/td[2]/div/div[2]/a[1] # 1st job apply button
//*[@id="startups_content"]/div[1]/div[5]/div/div/div[3]/div[2]/table/tbody/tr/td[2]/div/div[2]/a[1] # 2nd job apply button
//*[@id="layouts-base-body"]/div[13]/div/div/div/div/div/div[1]/div/div[2]/button # 2nd job send application
//*[@id="layouts-base-body"]/div[12]/div/div/div/div/div/div[1]/div/div[2]/button' # 1st job send application

jobs = driver.find_elements_by_class_name('header-info')
for job in jobs:
    job.click()


for i in range(3, 50):
    driver.find_element_by_xpath('//*[@id="startups_content"]/div[1]/div[5]/div/div/div['+str(i)+']').click()

    driver.find_element_by_xpath('//*[@id="startups_content"]/div[1]/div[5]/div/div/div['+str(i)+']/div[2]/table/tbody/tr/td[2]/div/div[2]/a[1]')
    driver.switch_to.frame

    applyjob = driver.find_element_by_xpath('//*[@id="layouts-base-body"]/div['+str(i+10)+']/div/div/div/div/div/div[1]/div/div[2]/button')
    if applyjob.is_enabled:
        applyjob.click()
        driver.implicitly_wait(10)
    else:
        driver.find_element_by_xpath('//*[@id="layouts-base-body"]/div['+str(i+10)+']/div/div/div/div/div/div[1]/div/div[2]/button').click()
    driver.switch_to_window
"""