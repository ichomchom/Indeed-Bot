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
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        # create a new Chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get('https://secure.indeed.com/account/login')

        # Get email field
        email_elem = self.driver.find_element(By.ID, 'signin_email')

        email_elem.send_keys(info.email)

        # Click the next button
        next_button = self.driver.find_element(By.ID, 'login-submit-button')
        next_button.click()

        # Get password field
        pass_elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'signin_password')))
        pass_elem.send_keys(info.password)
        pass_elem.submit()

        print('Logging in...')
        self.driver.implicitly_wait(10)

        # Redirect to main page
        self.driver.find_element_by_class_name('indeed-logo').click()

        # Close privacy policy
        self.driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div[2]/button').click()

        # get what field
        what_elem = self.driver.find_element_by_id('text-input-what')
        what_elem.clear()
        what_elem.send_keys(info.title)

        # get where field
        where_elem = self.driver.find_element_by_id('text-input-where')
        where_elem.send_keys(Keys.CONTROL, 'a')
        where_elem.send_keys(info.zipCode)
        where_elem.submit()

        # get list of jobs with apply by indeed only
        job_list = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "jobsearch-SerpJobCard")]')))

        # initialize main page
        main = self.driver.current_window_handle

        # Go through the jobList and open in new tab
        for job in job_list:
            job_title_elem = job.find_element(By.CLASS_NAME, 'jobtitle')
            job_title = job_title_elem.get_attribute('title')

            # Open job in new tab
            job_title_elem.click()

            # get new tab and switch to it
            WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
            job_win = [window for window in self.driver.window_handles if window != main][0]
            self.driver.switch_to.window(job_win)

            print(f'Applying job {job_title}')

            # Click on Apply Now
            apply_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="apply-button-container"]//button')))
            apply_button.click()

            # Close apply with indeed popup
            close_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "popover-x-button-close")]')))
            close_button.click()

            # Click continue on contact info page
            contact_continue_button = WebDriverWait(self.driver, 10).until(EC.element_located_selection_state_to_be_clickable((By.XPATH, '//button[contains(@class, "ia-continueButton ia-ContactInfo-continue css-vw73h2 e8ju0x51")]')))
            contact_continue_button.click()

            # Click continue on add resume for your employer page
            resume_continue_button = WebDriverWait(self.driver, 10).until(EC.element_located_selection_state_to_be_clickable((By.XPATH, '//button[contains(@class, "ia-continueButton ia-Resume-continue css-vw73h2 e8ju0x51")]')))
            resume_continue_button.click()

            # Click continue on add resume for your employer page
            question_continue_button = WebDriverWait(self.driver, 10).until(EC.element_located_selection_state_to_be_clickable((By.XPATH, '//button[contains(@class, "ia-continueButton ia-Question-continue css-vw73h2 e8ju0x51")]')))
            question_continue_button.click()

            # Click continue on add resume for your employer page
            relevant_job_continue_button = WebDriverWait(self.driver, 10).until(EC.element_located_selection_state_to_be_clickable((By.XPATH, '//button[contains(@class, "ia-continueButton ia-WorkExperience-continue css-vw73h2 e8ju0x51")]')))
            relevant_job_continue_button.click()

            # Click continue on add resume for your employer page
            review_application_button = WebDriverWait(self.driver, 10).until(EC.element_located_selection_state_to_be_clickable((By.XPATH, '//button[contains(@class, "ia-continueButton ia-SupportingDocument-continue css-vw73h2 e8ju0x51")]')))
            review_application_button.click()

            submit_application_button = WebDriverWait(self.driver, 10).until(EC.element_located_selection_state_to_be_clickable((By.XPATH, '//button[contains(@class, "ia-continueButton css-10eonrg e8ju0x51")]')))
            submit_application_button.click()

            # Go back to main page
            self.driver.close()
            self.driver.switch_to.window(main)

        print('All jobs applied to.')
        self.driver.quit()

if __name__ == '__main__':
    bot = IndeedBot()
