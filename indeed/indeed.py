
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options


options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')

import info
from info import *

import time, random

#these are the time intervals for the random sleep function
x = 5
y = 10

jobCounter = 0
pageCounter = 0

def delay(): 
    global x, y
    # time.sleep(random.randrange(x, y))

sign_in_class = '.çgnav-header-10stsit eu4oa1w0'
logo_id = 'indeed-globalnav-logo'
email_input_id = 'ifl-InputFormField-3'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://secure.indeed.com/auth?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F%3Ffrom%3Dgnav-util-homepage&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fwww.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess&_ga=2.133502215.883580095.1677254703-386616490.1675952228")

#give user time to sign in and set job description and location
time.sleep(120)

def login(): 
    # click on sign in
    delay()
    sign_in_btn = driver.find_element(By.CSS_SELECTOR, '.css-12ypvar')
    sign_in_btn.click()

    # click on PW input
    delay()
    pw_Input = driver.find_element(By.CSS_SELECTOR, '.css-5yee0j')
    pw_Input.click()

    # type password
    delay()
    ActionChains(driver) \
        .send_keys_to_element(pw_Input, info.password) \
        .perform()

    # click on sign in
    delay()
    sign_in_btn = driver.find_element(By.CSS_SELECTOR, '.css-12ypvar')
    sign_in_btn.click()

#get list of all easy apply jobs on the page
def get_jobs():
    delay()
    jobs = driver.find_elements(By.CSS_SELECTOR, '.jobsearch-SerpJobCard')
    return jobs

#apply to each job
def apply_to_jobs(jobs, jobCounter):
    for job in jobs:
        delay()
        job.click()
        delay()
        apply_btn = driver.find_element(By.CSS_SELECTOR, '.icl-Button--primary')
        apply_btn.click()
        delay()
        submit_btn = driver.find_element(By.CSS_SELECTOR, '.icl-Button--primary')
        submit_btn.click()
        jobCounter += 1

#go to next page
def next_page(pageCounter):
    delay()
    next_btn = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]')
    next_btn.click()
    pageCounter += 1

#for loop to go through 50 pages
for i in range(50):
    jobs = get_jobs()
    apply_to_jobs(jobs)
    print ('jobs applied to: ', jobCounter)
    next_page()

print(f'Applied to {jobCounter} jobs on {pageCounter} pages')