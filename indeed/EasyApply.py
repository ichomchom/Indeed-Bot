# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from fake_useragent import UserAgent
from indeed import Options


def continueButton():
    continueButton = driver.find_element(By.CLASS_NAME, 'ia-continueButton')
    continueButton.click()

# function to handle easy apply jobs
def easyApply():
    # contact info page
    delay()
    continueButton()

    # resume page
    delay()
    continueButton()

    # questions page
    delay()
    # count number of questions with class of ia-questions-items
    questions = driver.find_elements(By.CLASS_NAME, 'ia-Questions-item')

    # loop through questions and answer them
    numberOfQuestions = len(questions) - 1
    for i in range(numberOfQuestions):
        # find the question
        
    for()