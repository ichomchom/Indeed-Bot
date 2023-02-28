import os
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

#set these up in a .env file in the gitignore so your info is not on github.


# input.py get users input 
email = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')


#this info can stay here (its public on github though)

position = 'software engineer'

zipCode = '10018'
name = 'John Hurley'
phone = '(321) 394-6133'
linkedinURL = 'https://www.linkedin.com/in/john-hurley-aa0179b2/'