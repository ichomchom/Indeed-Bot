from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://www.indeed.com/')

driver.find_element_by_xpath('//*[@id="text-input-what"]').send_keys('software engineer')
whereElem = driver.find_element_by_xpath('//*[@id="text-input-where"]')
whereElem.send_keys(Keys.CONTROL, 'a')
whereElem.send_keys('91101')
whereElem.submit()

jobList = driver.find_elements_by_class_name('iaP')
action = ActionChains(driver)

main = driver.window_handles[0]
for job in jobList:
    job.click()
    jobWin = driver.window_handles[1]
    driver.switch_to_window(jobWin)
    driver.find_element_by_class_name('jobsearch-IndeedApplyButton-contentWrapper').click()
    

    

"""
#driver.find_element_by_class_name('jobsearch-IndeedApplyButton-contentWrapper').click()
driver.find_element_by_xpath('//*[@id="indeedApplyButtonContainer"]/span/div[1]/button/div').click()


#Get popup window
main_window = None
while not main_window:
    main_window = driver.current_window_handle
popup_window = None

while not popup_window:
    for handle in driver.window_handles:
        if handle != main_window:
            popup_window = handle
            break

#iframe = driver.find_element_by_xpath('/html/body/iframe')
iframe = driver.find_element_by_css_selector('body > iframe')

title = driver.title
print(title)
driver.switch_to_frame

driver.implicitly_wait(10)

driver.find_element_by_id('input-applicant.name').send_keys('Huey Phan')


#nameElem = driver.find_element_by_id('input-applicant.name')
#nameElem.send_keys('Huey Phan')

driver.find_element_by_id('input-applicant.email').send_keys('phan.huey389@gmail.com')
"""