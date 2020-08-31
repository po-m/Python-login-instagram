from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

___username = 'amora1bewixon73903'
___password = 'jBteeAWNQ8Fle3'
____new_username = 'weweb242g3'

NUM_OF_NAME = 2
NUM_OF_SURNAME = 2
NUM_OF_ACCOUT = 1

def parse_name():
  name = []

  with open('name.txt', 'r') as data:
    for line in data:
      parser_name = line[:-1]
      name.append(parser_name)
  return name[random.randrange(0, NUM_OF_NAME)]

def parse_surname():
  surname = []

  with open('surname.txt', 'r') as data:
    for line in data:
      parser_surname = line[:-1]
      surname.append(parser_surname)
  return surname[random.randrange(0, NUM_OF_SURNAME)]

def create_a_user():
  to_name = parse_name() + ' ' + parse_surname()
  #to_username = parse_name() + parse_surname()
  print(to_name) 
  #print(to_username)

def parser_account():
  username = []
  password = []

  with open('account.txt', 'r') as data:
    for line in data:
      line = line.strip()
      parser_username, parser_password = line.split(':')
      username.append(parser_username)
      password.append(parser_password)
  return username, password

def login():
  username, password = parser_account()
  user = create_a_user()
  
  for i in range(0, NUM_OF_ACCOUT):
    browser = webdriver.Chrome('chromedriver')

    browser.get('https://www.instagram.com/')
    time.sleep(random.randrange(3, 5))

    username_input = browser.find_element_by_name('username')
    username_input.clear()
    username_input.send_keys(username)

    time.sleep(2)

    password_input = browser.find_element_by_name('password')
    password_input.clear()
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    time.sleep(2)

    browser.get("https://www.instagram.com/accounts/edit/")

    input_new_username = browser.find_element_by_id('pepName')
    input_new_username.clear()
    input_new_username.send_keys(user)

    input_new_second_username = browser.find_element_by_id('pepUsername')
    input_new_second_username.clear()
    input_new_second_username.send_keys(user)

    time.sleep(2)

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[11]/div/div/button').click()

    print('User: ' + user)

    time.sleep(1000)

def main():
  create_a_user()

main()
