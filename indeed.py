
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

import info
from info import *

import time, random

delay = random.randrange(5, 10)


sign_in_class = '.çgnav-header-10stsit eu4oa1w0'
logo_id = 'indeed-globalnav-logo'
email_input_id = 'ifl-InputFormField-3'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://secure.indeed.com/auth?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F%3Ffrom%3Dgnav-util-homepage&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fwww.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess&_ga=2.133502215.883580095.1677254703-386616490.1675952228")

# locate email input
driver.implicitly_wait(30)
email_input = driver.find_element(by=By.ID, value=email_input_id)
email_input.click()

# write into email input
ActionChains(driver) \
    .send_keys_to_element(email_input, info.email) \
    .perform()

# click on continue
continue_button = driver.find_element(By.CSS_SELECTOR,".css-jorj5j")
continue_button.click()

# click continue with google
# continue_google = driver.find_element(By.CSS_SELECTOR,".css-pahgg8")
# continue_google.click()

# click log in with password
Btn = driver.find_element(By.CSS_SELECTOR, '.css-1imtygv')
Btn.click()

# click on PW input
pw_Input = driver.find_element(By.CSS_SELECTOR, '.css-5yee0j')
pw_Input.click()

# type password
ActionChains(driver) \
    .send_keys_to_element(pw_Input, info.password) \
    .perform()

# click on sign in
sign_in_btn = driver.find_element(By.CSS_SELECTOR, '.css-12ypvar')
sign_in_btn.click()

time.sleep(999)