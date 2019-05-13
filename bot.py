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
        

IndeedBot()