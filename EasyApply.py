# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from info import *
import random
import time


# initialize delay function which will return a random value between 3 and 7 seconds
def delay():
    time.sleep(random.uniform(3,7))

def textInputQuestion(currentQuestion, driver): 
     
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

def continueButton(driver):
    continueButton = driver.find_element(By.CLASS_NAME, 'ia-continueButton')
    continueButton.click()

# function to handle easy apply jobs
def easyApply(driver):
    print('beginning easy apply process')
    # contact info page
    delay()
    continueButton()
    print('clicked continue button on contact info page')

    # resume page
    delay()
    continueButton()
    print('clicked continue button on resumé page')

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
    
    delay()
    continueButton()
    print('clicked continue button on questions page')

    # add job with relevant experience 
    delay()
    continueButton()
    print('clicked continue button on add job page')

    # click submit 
    delay()
    continueButton()
    print('clicked continue button on submit page')

    # close current tab
    driver.close()
    print('closed current tab')

