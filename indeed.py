
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
import info
from info import *
import time
from EasyApply import *

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://secure.indeed.com/auth?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F%3Ffrom%3Dgnav-util-homepage&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fwww.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess&_ga=2.133502215.883580095.1677254703-386616490.1675952228")


def terminalLogger(sleepTime=0.5, message=''):
    print(message)
    time.sleep(sleepTime)
    print('\n')


####### time for user to login manually
driver.implicitly_wait(999)

# locate email input
terminalLogger(message='Locating email input...')
email_input = driver.find_element(by=By.ID, value='ifl-InputFormField-3')
email_input.click()

# write into email input
terminalLogger(message='typing email...')
ActionChains(driver) \
    .send_keys_to_element(email_input, info.email) \
    .perform()

# click log in with password
terminalLogger(message='Click log in with password instead...', sleepTime=1)
Btn = driver.find_element(By.CSS_SELECTOR, '.css-1imtygv')
Btn.click()

# click on PW input
terminalLogger(message='Focus on password input')
pw_Input = driver.find_element(By.CSS_SELECTOR, '.css-5yee0j')
pw_Input.click()

# type password
terminalLogger(message='Typing password...')
ActionChains(driver) \
    .send_keys_to_element(pw_Input, info.password) \
    .perform()


######### Input job search params
terminalLogger(message='typing search inputs')
what_input = driver.find_element(by=By.ID, value='text-input-what')
where_input = driver.find_element(by=By.ID, value='label-text-input-where')

what_input.click()
ActionChains(driver) \
    .send_keys_to_element(what_input, info.position) \
    .perform()

# where_input.click()
# ActionChains(driver) \
#     .send_keys_to_element(where_input, info.where) \
#     .perform()

search_button = driver.find_element(by=By.CLASS_NAME, value='yosegi-InlineWhatWhere-primaryButton')
search_button.click()



########
posts_list = driver.find_element(by=By.CLASS_NAME, value='jobsearch-ResultsList')
posts = posts_list.find_elements(by=By.CLASS_NAME, value='jcs-JobTitle')
print(len(posts))

rightPane = driver.find_element(by=By.CSS_SELECTOR, value='div.jobsearch-RightPane')

def checkEasyApply(driver=driver):
    driver.implicitly_wait(30)
    time.sleep(5)
    # application_btn = driver.find_element(by=By.CLASS_NAME, value='css-v0a1gu')
    # application_btn = driver.find_element(by=By.CLASS_NAME, value='css-1hjxf1u')

    # application_btn = driver.find_elements(by=By.CSS_SELECTOR, value='.jobsearch-IndeedApplyButton-newDesign')
    # if len(application_btn) == 0:
    #     pass
    # else:
    #     print(application_btn[0].text)
    #     application_btn[0].click()

    try:
        print('finding apply button..')
        application_btn = rightPane.find_element(by=By.CSS_SELECTOR, value='button.css-1bm49rc.e8ju0x51')
        application_btn.click()
        terminalLogger(message='Easy Apply button found')
        easyApply(driver)
    except:
        terminalLogger(message='Easy Apply button not found') 
        pass


for post in posts:
    post.click()
    checkEasyApply(driver=driver)
    time.sleep(3)

terminalLogger(message='end script in 5', sleepTime=5)

driver.quit()
####################################################### Scratched for manual sign in


#
# # click on continue
# continue_button = driver.find_element(By.CSS_SELECTOR,".css-jorj5j")
# continue_button.click()
#
# # click continue with google
# # continue_google = driver.find_element(By.CSS_SELECTOR,".css-pahgg8")
# # continue_google.click()
#
# # click log in with password
# Btn = driver.find_element(By.CSS_SELECTOR, '.css-1imtygv')
# Btn.click()
#
# # click on PW input
# pw_Input = driver.find_element(By.CSS_SELECTOR, '.css-5yee0j')
# pw_Input.click()
#
# # type password
# ActionChains(driver) \
#     .send_keys_to_element(pw_Input, info.password) \
#     .perform()
#
# # click on sign in
# sign_in_btn = driver.find_element(By.CSS_SELECTOR, '.css-12ypvar')
# sign_in_btn.click()

#############################################

time.sleep(999)