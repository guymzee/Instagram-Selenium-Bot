from art import *
import pandas as pd
import random
from random import randint
from time import sleep, strftime
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
from tqdm import tqdm_gui
import sys
sys.path.insert(0, './utils/')
import secret

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
sleep(2)
button_login = webdriver.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button')
button_login.click()
sleep(10)

notnow = webdriver.find_element_by_css_selector(
    'button.aOOlW:nth-child(2)')
notnow.click()  # comment these last 2 lines out, if you don't get a pop up asking about notifications

hashtag_list = ['autoflowercommunity', 'oklahomamedicalcannabis', 'homegrowncannabis', 'indoorgrow']

# setting optioins to 0

likes = 0
comments = 0
tag = -1
stories_watched = 0

# setting comments
sleep(2)
watch_all_stories_btn = webdriver.find_element_by_xpath(
    "/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div")
watch_all_stories_btn.click()
sleep(2)
try:
    while webdriver.find_element_by_css_selector(".ow3u_"):
        watch_all_stories_next = webdriver.find_element_by_css_selector(".ow3u_")
        watch_all_stories_next.click()
        sleep(randint(2, 3))
        stories_watched += 1
        print("stories watched: {}".format(stories_watched))
except NoSuchElementException:
    for hashtag in hashtag_list:
        sleep(2)
        tag += 1
        webdriver.get('https://www.instagram.com/explore/tags/' +
                    hashtag_list[tag] + '/')
        image_img=webdriver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]')
        sleep(1)
        image_img.click()
        sleep(1)
        
        while likes <= 12:  # set max number of likes per hashtag here
            sleep(1)
            print("trying to like image...")
            image_like_svg=webdriver.find_element_by_css_selector(
                '.fr66n > button:nth-child(1) > svg:nth-child(1)')
            image_like_label=image_like_svg.get_attribute("aria-label")
            if image_like_label == "Like":
                image_like_svg.click()
                likes += 1
                print('liked images: {}'.format(likes))
                sleep(randint(5, 15))  # random timer here
                image_next=webdriver.find_element_by_xpath(
                    '/html/body/div[4]/div[1]/div/div/a[2]')
                image_next.click()
                sleep(randint(2, 3))  # random timer here
            else:
                print('image already liked')
                image_next=webdriver.find_element_by_xpath(
                    '/html/body/div[4]/div[1]/div/div/a[2]')
                image_next.click()
                sleep(1)  # random timer here
        else:
            print('finished like process')
            print('total liked images: {}'.format(likes))
            sleep(2)
            print('moving on to the next process...')
            image_close=webdriver.find_element_by_xpath(
                '/html/body/div[4]/div[3]/button')
            sleep(2)
            image_close.click()
            sleep(2)

        image_img=webdriver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]')
        sleep(2)
        image_img.click()
        
        while comments <= 2:  # set max number of comment per hashtag here
            all_comments = []
            comment_by_user = webdriver.find_elements_by_class_name('TlrDj')
            
            for i in comment_by_user:
                all_comments.append(i.get_attribute('title'))

            if any(x == secret.username for x in all_comments):
                sleep(2)
                image_next=webdriver.find_element_by_xpath(
                '/html/body/div[4]/div[1]/div/div/a[2]')
                image_next.click()
                sleep(2)
            else:
                print("no comment")
                sleep(2)
                comment_list=['nice one 👍🏼', 'great! 🚀',
                            'Amazing 😍', 'Looking great!', 'so cool!!! 😳', '🔥🔥🔥🔥', '😍😍😍', '🧬 Great Stuff!!']
                comment_item=random.choice(comment_list)

                sleep(randint(1, 5))  # random timer here

                comment_box=ui.WebDriverWait(webdriver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea")))
                webdriver.execute_script(
                    "arguments[0].scrollIntoView(true);", comment_box)

                (
                    ActionChains(webdriver)
                    .move_to_element(comment_box)
                    .click()
                    .send_keys(comment_item)
                    .perform()
                )

                sleep(2)

                send_comment=webdriver.find_element_by_xpath(
                    "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button")
                send_comment.click()
                comments += 1
                print('images commented: {}'.format(comments))
                sleep(25)
                sleep(randint(5, 10))  # random timer here
        likes=0
        comments=0
