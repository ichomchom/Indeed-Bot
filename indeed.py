from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import info


class IndeedBot:
    def __init__(self):
        # Create headless chrome
        options = Options()
        # options.headless = True

        # create a new Chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get('https://secure.indeed.com/account/login')

        # Get email field
        emailElem = self.driver.find_element(By.ID, 'ifl-InputFormField-3')

        emailElem.send_keys(info.email)

        # click log in with password button
        loginWithPasswordButton = self.driver.find_element(By.ID, 'auth-page-google-password-fallback')
        loginWithPasswordButton.click()

        # Get password field
        passElem = self.driver.find_element(By.ID, 'ifl-InputFormField-21')
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
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_3_31R))).click()

            # Close apply with indeed popup
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "popover-x-button-close"))).click()

            # Fill out job application
            # TODO: Add code to fill out job application

            # Go back to main page
            self.driver.close()
            self.driver.switch_to.window(main)

        print('All jobs applied to.')
        self.driver.quit()
