from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.indeed.com/cmp/CoolHandle/jobs/Lamp-Software-Engineer-f11e3756c33910cf?sjdu=QwrRXKrqZ3CNX5W-O9jEvfT7_GX3aVyUY5cAEFDiEwXX1AHSy2SWqnU9P3rRZWrvzP3gbk5VsieJTx4bHuMrm85ZJsAFzqeyuNLColJH-wA&tk=1db276ktu1t4t003&adid=290534037&vjs=3')
#driver.find_element_by_class_name('jobsearch-IndeedApplyButton-contentWrapper').click()
driver.find_element_by_xpath('//*[@id="indeedApplyButtonContainer"]/span/div[1]/button/div').click()

"""
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
"""
iframe = driver.find_element_by_xpath('/html/body/iframe')
driver.switch_to_frame(iframe)
driver.find_element_by_id('form-action-continue').click()

nameElem = driver.find_element_by_id('input-applicant.name')
nameElem.send_keys('Huey Phan')

driver.find_element_by_id('input-applicant.email').send_keys('phan.huey389@gmail.com')
