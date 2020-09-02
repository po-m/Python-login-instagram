from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


# save new username with old password to new .txt file, cz 1st used username will'be lost, cz it will be replaced
# add adder to photos

NUM_OF_NAME = 2700
NUM_OF_SURNAME = 2700
NUM_OF_ACCOUT = 3
NUM_OF_NUM = 3
NUM_OF_MAX_NUM = 9
ACCOUNT_PATH = 'data/account.txt'
NAME_PATH = 'data/name.txt'
SURNAME_PATH = 'data/surname.txt'
NEW_ACCOUNT = 'data/new_account.txt'
INSTAGRAM_INDEX_PATH = 'https://www.instagram.com/'
INSTAGRAM_EDIT_PATH = 'https://www.instagram.com/accounts/edit/'

def parser_name():
  name = []
  with open(NAME_PATH, 'r') as data:
    for line in data:
      parser_name = line[:-1]
      name.append(parser_name)
  return name[random.randrange(0, NUM_OF_NAME)]

def parser_surname():
  surname = []
  with open(SURNAME_PATH, 'r') as data:
    for line in data:
      parser_surname = line[:-1]
      surname.append(parser_surname)
  return surname[random.randrange(0, NUM_OF_SURNAME)]

def create_new_username():
  random_list = []
  for i in range(0, NUM_OF_NUM):
    number = random.randint(1, NUM_OF_MAX_NUM)
    random_list.append(number)
  return parser_name() + '_' + parser_surname() + str(random_list[0]) + str(random_list[1]) + str(random_list[2])

def parser_account():
  username = []
  password = []
  with open(ACCOUNT_PATH, 'r') as data:
    for line in data:
      line = line.strip()
      parser_username, parser_password = line.split(':')
      username.append(parser_username)
      password.append(parser_password)
  return username, password

def save():
  test = parser_account()
  new_username = create_new_username()

  new_file = open(NEW_ACCOUNT, 'w')
  new_file.write(new_username + ':' + test[1][0])
  #new_file.write(test[0][0] + ':' + test[1][0])

def login():
  test = parser_account()
  new_username = create_new_username()
  
  username = test[0][0]
  password = test[1][0]

  #for i in range(0, NUM_OF_ACCOUT):
  browser = webdriver.Chrome('chromedriver')

  browser.get(INSTAGRAM_INDEX_PATH)
  time.sleep(random.randrange(3, 5))

  print('Username: ' + str(username))
  username_input = browser.find_element_by_name('username')
  username_input.clear()
  username_input.send_keys(username)
  

  time.sleep(2)

  print('Password: ' + str(password))
  password_input = browser.find_element_by_name('password')
  password_input.clear()
  password_input.send_keys(password)
  password_input.send_keys(Keys.ENTER)

  time.sleep(2)

  browser.get(INSTAGRAM_EDIT_PATH)

    # input_new_username = browser.find_element_by_id('pepName')
    # input_new_username.clear()
    # input_new_username.send_keys(user)

  print('New username: ' + str(new_username))
  input_new_second_username = browser.find_element_by_id('pepUsername')
  input_new_second_username.clear()
  input_new_second_username.send_keys(new_username)

  #time.sleep(2)

    #browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[11]/div/div/button').click()

def main():
  save()

main()
