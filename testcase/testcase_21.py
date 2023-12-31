from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from dotenv import load_dotenv
import logging
import re
import random

load_dotenv()
logging.basicConfig(filename='./logs/testcase_21.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
action = ActionChains(driver)
website_url = "http://teststore.automationtesting.co.uk"
current =''
def float_value(s):
    return float(s[1:])


def visit_website():
    driver.get(website_url)

def check_breadcrumb():
    current_breadcumb = driver.find_elements(By.CSS_SELECTOR,'ol li a span')[-1]
    if current_breadcumb.text.replace(' ','').lower() in current:
        logging.info(f"Test pass: Nav {current} worked")
    else:
        logging.error(f'Test fail: Nav {current} fail')
    
def click_nav():
    global current
    n = len(driver.find_elements(By.CSS_SELECTOR,'div.menu ul#top-menu li a'))
    for i in range(n):
        nav_buttons = driver.find_elements(By.CSS_SELECTOR,'div.menu ul#top-menu li a')
        current = nav_buttons[i].text.replace(' ','').replace('\n','').lower()
        if current!= '':
            nav_buttons[i].click()
            time.sleep(2)
            check_breadcrumb()  
    
def testcase_21():
    visit_website()
    click_nav()
    
    

    

if __name__ == "__main__":
    testcase_21()