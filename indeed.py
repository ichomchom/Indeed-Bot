from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import info

class IndeedBot:
    def __init__(self):

        # Create headless chrome
        options = Options()
        #options.headless = True

        # create a new Chrome session
        self.driver = webdriver.Chrome('./chromedriver.exe')


        # open indeed
        self.driver.get('https://secure.indeed.com/account/login')

        # Get email field
        emailElem = self.driver.find_element_by_id('login-email-input')
        emailElem.send_keys(info.email)

        # Get password field
        passElem = self.driver.find_element_by_id('login-password-input')
        passElem.send_keys(info.password)
        passElem.submit()

        print('Logging in...')
        self.driver.implicitly_wait(10)

        # Redirect to main page
        self.driver.find_element_by_class_name('icl-DesktopGlobalHeader-logoLink').click()

        # Close privacy policy
        self.driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div[2]/button').click()

        # get what field
        whatElem = self.driver.find_element_by_id('text-input-what')
        #whatElem.clear()
        whatElem.send_keys(info.title)

        # get where field
        whereElem = self.driver.find_element_by_id('text-input-where')
        whereElem.send_keys(Keys.CONTROL, 'a')
        whereElem.send_keys(info.zipCode)
        whereElem.submit()
 
        # get list of jobs with apply by indeed only
        jobList = self.driver.find_elements_by_class_name('iaP')

        # initialize main page
        main = self.driver.window_handles[0]

        # Go through the jobList and open in new tab
        for job in jobList:
            job.click()

            # get new tab and switch to it
            jobWin = self.driver.window_handles[1]
            self.driver.switch_to.window(jobWin)
            title = self.driver.title
            print('Applying job ' + title)

            # Click on Apply Now
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'jobsearch-IndeedApplyButton-contentWrapper'))).click()

            # Locate the parent iframe and switch to it
            parentIframe = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,"//iframe[contains(@id,'modal-iframe')]")))    
            self.driver.switch_to.frame(parentIframe)

            # Locate the parent iframe and switch to it
            childIframe =  WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,"//iframe[contains(@src,'resumeapply')]")))
            self.driver.switch_to.frame(childIframe)   
            conButton = self.driver.find_element_by_xpath('//*[@id="form-action-continue"]')
            # Click on continue button if there any             
            if conButton.is_enabled():
                self.driver.implicitly_wait(30)
                conButton.click()
                if conButton.is_enabled():
                    self.driver.close()
                    self.driver.switch_to.window(main) 
                else:
                    WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="form-action-submit"]'))).click()
                    self.driver.close()
                    self.driver.switch_to.window(main) 
            

            #If no button close the window and switch to main window
            #WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-action-submit"]'))).click()
            #if self.driver.find_element_by_xpath('//*[@id="ia-container"]/div/div[2]/a'):
            else: 
                self.driver.close()
                self.driver.switch_to.window(main)
 



IndeedBot()
