from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import info
class IndeedBot:
    def __init__(self):

        # create a new Firefox session
        self.driver = webdriver.Firefox()

            # open indeed
        self.driver.get('https://secure.indeed.com/account/login')

        # Get email field
        emailElem = self.driver.find_element_by_id('login-email-input')
        emailElem.send_keys(info.email)

        # Get password field
        passElem = self.driver.find_element_by_id('login-password-input')
        passElem.send_keys(info.passwd)
        passElem.submit()

        # Redirect to main page
        self.driver.find_element_by_class_name('icl-Logo').click()
        

        # get what field
        whatElem = self.driver.find_element_by_id('text-input-what')
        whatElem.clear()
        whatElem.send_keys(info.title)

        # get where field
        whereElem = self.driver.find_element_by_id('text-input-where')
        whereElem.send_keys(Keys.CONTROL, 'a')
        whereElem.send_keys(info.zipCode)
        whereElem.submit()
        
        # TODO: get apply job with indeed only
        # <div class="iaP">
        # <span class="iaLabel">Apply with your Indeed Resume</span>
        
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
