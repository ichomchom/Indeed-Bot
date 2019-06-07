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

# Headless chrome driver
options = Options()
#options.headless = True

# Create chrome driver
driver = webdriver.Chrome(options = options)


# Open the driver and go to angel.co
driver.get('https://angel.co/')

# Find the log in button
driver.find_element_by_xpath("//a[@href='/login']").click()

# Fill out email and password for login
driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(info.email)
driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(info.password)
driver.find_element_by_xpath('//*[@id="new_user"]/div[2]/input').click()


driver.implicitly_wait(30)

# Get number of jobs
remain = driver.find_element_by_xpath('//*[@id="startups_content"]/div[1]/div[2]/div[1]/div[2]/div[1]/span').text

for i in range(int(remain)):
 
    # Find the blue button to apply
    driver.find_element_by_xpath("(//a[contains(.,'Apply Now')])[1]").click()

    # Fill out Cover Letter
    note = driver.find_element_by_xpath('//*[@id="layouts-base-body"]/div[13]/div/div/div/div/div/div[1]/div/textarea')
    companyName = driver.find_element_by_class_name('startup-title').text[9::]
    position = driver.find_element_by_class_name('job-title').text
    
    note.send_keys(content % (position, companyName, info.phone, info.email, info.name))

    print('Apply for ' + position + ' at' + companyName + '.....')

    driver.implicitly_wait(10)
    # Find the xpath for the apply button
    apply = driver.find_element_by_xpath("//button[contains(.,'Send Application')]")

    # Check if the apply button available or not
    if apply.is_enabled:
        apply.click()
        driver.implicitly_wait(10)
    else:
        # If not available click cancel
        driver.find_element_by_xpath("//button[contains(., 'Cancel')]").click()

    #Close the popup frame
    driver.find_element_by_xpath("//button[contains(.,'Close')]").click()
    
    print('Done...')
    
    #Refresh browser to reapply the job
    driver.refresh()

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