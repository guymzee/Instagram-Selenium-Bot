from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep, strftime
from random import randint
import random
import pandas as pd
from art import *
import secret


from tqdm import tqdm


tprint("Instagram")
tprint("Bot")
sleep(2)
print("Made with Selenium")
sleep(1)
print("Version 1.0")
print("Loading Scripts...")
for i in tqdm(range(100)):
    sleep(0.01)
    pass

chromedriver_path = './geckodriver'  # Change this to your own chromedriver path!
webdriver = webdriver.Firefox(executable_path="./geckodriver")
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys(secret.username)
password = webdriver.find_element_by_name('password')
password.send_keys(secret.password)

button_login = webdriver.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button')
button_login.click()
sleep(8)

notnow = webdriver.find_element_by_xpath(
    '/html/body/div[4]/div/div/div[3]/button[2]')
notnow.click()  # comment these last 2 lines out, if you don't get a pop up asking about notifications

tag = -1

hashtag_list = ['amnesiahazeauto']

tag += 1
webdriver.get('https://www.instagram.com/explore/tags/' +
              hashtag_list[tag] + '/')
image_img = webdriver.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]')
sleep(1)
image_img.click()
sleep(1)

# setting optioins to 0

likes = 0
comments = 0

# setting comments


while likes <= 10:  # set max number of likes per hashtag here
    image_like = webdriver.find_element_by_xpath(
        '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
    image_like.click()
    sleep(randint(1, 5))  # random timer here
    image_next = webdriver.find_element_by_xpath(
        '/html/body/div[4]/div[1]/div/div/a[2]')
    image_next.click()
    sleep(randint(2, 3))  # random timer here
    likes += 1
    print('liked images: {}'.format(likes))
else:
    print('finished like process')
    print('total liked images: {}'.format(likes))
    sleep(1)
    print('moving on to the next process...')
    image_close = webdriver.find_element_by_xpath(
        '/html/body/div[4]/button[1]')
    image_close.click()
    sleep(2)

image_img = webdriver.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]')
sleep(1)
image_img.click()
while comments <= 4:  # set max number of comment per hashtag here

    comment_list = ['nice one 👍🏼', 'great! 🚀',
                    'Amazing 😍', 'Looking great!', 'so cool!!! 😳', '🔥🔥🔥🔥', '😍😍😍', '🧬 Great Stuff!!']
    comment_item = random.choice(comment_list)

    sleep(randint(1, 5))  # random timer here

    comment_box = ui.WebDriverWait(webdriver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea")))
    webdriver.execute_script("arguments[0].scrollIntoView(true);", comment_box)

    (
        ActionChains(webdriver)
        .move_to_element(comment_box)
        .click()
        .send_keys(comment_item)
        .perform()
    )

    sleep(2)

    send_comment = webdriver.find_element_by_xpath(
        "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button")
    send_comment.click()

    sleep(25)
    sleep(randint(5, 10))  # random timer here
    image_next = webdriver.find_element_by_xpath(
        '/html/body/div[4]/div[1]/div/div/a[2]')
    image_next.click()
    comments += 1
    print('images commented: {}'.format(comments))
