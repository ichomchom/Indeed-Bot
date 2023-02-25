# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from fake_useragent import UserAgent
from indeed import Options
from info import *

def textInputQuestion(currentQuestion): 
     
    # write the if statement to handle all text input questions where the answer is no
    if 'Do you need' in currentQuestion:
        delay()
        answer = driver.find_element(By.TAG_NAME, 'textarea')
        answer.send_keys('No')
    
    if 'linkedin' or 'LinkedIn' in currentQuestion:
        delay()
        answer = driver.find_element(By.TAG_NAME, 'textarea')
        answer.send_keys('linkedinURL')

    else:
        delay()
        answer = driver.find_element(By.TAG_NAME, 'textarea')
        answer.send_keys('Yes')

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

    counter = 0

    # loop through questions and answer them
    numberOfQuestions = len(questions) - 1
    for i in range(numberOfQuestions):
        currentQuestion = questions[counter].text
        
        # check if it is a text input question or a radio button question
        if 'ia-Answer-input' in currentQuestion:
            textInputQuestion(currentQuestion)

        counter += 1

    # add job with relevant experience 
    delay()
    continueButton()

    # click submit 
    delay()
    continueButton()
