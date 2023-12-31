from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
import logging
import re

load_dotenv()
logging.basicConfig(filename='./logs/testcase_8.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
website_url = "http://teststore.automationtesting.co.uk/3-clothes"

def float_value(s):
    return float(s[1:])


def visit_website():
    driver.get(website_url)



def filter():
    men_filter = driver.find_elements(By.CSS_SELECTOR,"ul.category-sub-menu li a")
    for filter in men_filter:
        if 'Men' in filter.text:
            filter.click()
            return

def check_filtered():
    try:
        men_category = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.block-category h1")))
        if men_category.text.lower() == 'Men'.lower():
            logging.info("Test pass: Men filter worked")
        else:
            logging.error("Test fail: Men filter didn't work")
    except:
        logging.error("Test fail: Men filter didn't work")
    


def testcase_8():
    visit_website()
    filter()
    check_filtered()
    
    

    

if __name__ == "__main__":
    testcase_8()