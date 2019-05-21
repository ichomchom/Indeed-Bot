from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import info

class IndeedBot:
    def __init__(self):

        # Create headless chrome
        options = Options()
        options.headless = True

        # create a new Chrome session
        self.driver = webdriver.Chrome(options=options)


        # open indeed
        self.driver.get('https://secure.indeed.com/account/login')

        # Get email field
        emailElem = self.driver.find_element_by_id('login-email-input')
        emailElem.send_keys(info.email)

        # Get password field
        passElem = self.driver.find_element_by_id('login-password-input')
        passElem.send_keys(info.password)
        passElem.submit()

        self.driver.implicitly_wait(10)

        # Redirect to main page
        self.driver.find_element_by_class_name('icl-DesktopGlobalHeader-logoLink').click()


        # get what field
        whatElem = self.driver.find_element_by_id('text-input-what')
        #whatElem.clear()
        whatElem.send_keys(info.title)

        # get where field
        whereElem = self.driver.find_element_by_id('text-input-where')
        whereElem.send_keys(Keys.CONTROL, 'a')
        whereElem.send_keys(info.zipCode)
        whereElem.submit()
        
        # TODO: get apply job with indeed only
        # <div class="iaP">
        # <span class="iaLabel">Apply with your Indeed Resume</span>
        #self.driver.find_element_by_class_name('iaP').click()

        #jobList = self.driver.find_element_by_class_name('jobsearch-SerpJobCard unifiedRow row result clickcard')
        
        # Job with apply by indeed
        jobList = self.driver.find_elements_by_class_name('iaP')

        # Go through the jobList and open in new tab
        for job in jobList:
            job.click()

            self.driver.find_element_by_xpath('//*[@id="indeedApplyButtonContainer"]/span/div[1]/button/div').click()
            
            #self.driver.implicitly_wait(10)
            
            #self.driver.find_element_by_id('input-applicant.name').send_keys(info.name)
            #self.driver.find_element_by_id('input-applicant.email').send_keys(info.email)

            #self.driver.find_element_by_class_name('icl-Button icl-Button--primary icl-Button--lg icl-u-xs-my--sm ia-FormActionButtons-continue').click()
            #self.driver.find_element_by_class_name('icl-Button icl-Button--primary icl-Button--lg icl-u-xs-my--sm ia-FormActionButtons-submit').click()
            jobTitle = self.driver.find_element_by_class_name('icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title')
            print(jobTitle)
        print(jobList)




        # TODO: get job card
        # class="jobsearch-SerpJobCard unifiedRow row result clickcard"
        
        # TODO: click apply job
        # class="indeed-apply-button-label"
        
        # TODO: Cover letter
        # icl-Button icl-Button--transparent icl-Button--sm ia-AddCoverLetter-button
        
        # TODO: Cover letter text box
        # id="textarea-applicant.applicationMessage"
        
        # TODO: Get job title
        # <div class="ia-JobInfoHeader-title">
        
        # TODO: Get company name
        # <div class="ia-JobInfoHeader-subtitle">
        
        # TODO: Used job title and company name add to cover leter, then submit
        
        # TODO: Apply Job
        # form-action-submit
        
        # TODO: Close popup window and continue apply
        # close-popup button_content
        
        # TODO: next page
        # <span class="np">Next&nbsp;»</span>
IndeedBot()
