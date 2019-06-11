from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://www.indeed.com/')

driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div[2]/button').click()

driver.find_element_by_xpath('//*[@id="text-input-what"]').send_keys('software engineer')
whereElem = driver.find_element_by_xpath('//*[@id="text-input-where"]')
whereElem.send_keys(Keys.CONTROL, 'a')
whereElem.send_keys('91101')
whereElem.submit()

jobList = driver.find_elements_by_class_name('iaP')
action = ActionChains(driver)

# Get the main page with window handles
main = driver.window_handles[0]

# Open new window for each jobs found
for i in range(1, len(jobList)):
    jobList[i].click()

    # assign new window just opened
    jobWin = driver.window_handles[i]

    # Switch to new window
    driver.switch_to.window(jobWin)

    driver.implicitly_wait(10)
    # Click apply job
   

    driver.find_element_by_class_name('jobsearch-IndeedApplyButton-contentWrapper').click()
    

    #iframe = driver.find_element_by_xpath('/html/body/iframe')
    #WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'resumeapply')]")))
    parentIframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//iframe[contains(@id,'modal-iframe')]")))    
    driver.switch_to.frame(parentIframe)

    childIframe =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//iframe[contains(@src,'resumeapply')]")))
    driver.switch_to.frame(childIframe)   

    #driver.find_element_by_xpath('//*[@id="input-applicant.name"]').send_keys('phan.huey398@gmail.com')
    #driver.find_element_by_xpath('//*[@id="form-action-cancel"]').click()

    # Close the current tab
    #driver.close()

    #driver.switch_to.window(main)
    #driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@id="indeedApplyButtonContainer"]/span/div[1]/button/div').click()

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




#nameElem = driver.find_element_by_id('input-applicant.name')
#nameElem.send_keys('Huey Phan')

driver.find_element_by_id('input-applicant.email').send_keys('phan.huey389@gmail.com')
"""