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
logging.basicConfig(filename='./logs/testcase_5.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
website_url = "http://teststore.automationtesting.co.uk/2-home"



def visit_website():
    driver.get(website_url)

def filter(number):
    try:
        filters = driver.find_elements(By.CSS_SELECTOR,"label.facet-label a")
        filters[number].click()
        time.sleep(3)
        logging.info("Test pass: Filter was selected")
    except:
        logging.error("Test fail: Filter wasn't selected")


def clear_each_filter(number):
    try:
        for i in range(number):
            driver.find_elements(By.CSS_SELECTOR,'li.filter-block a.js-search-link i')[0].click()
            time.sleep(3)
        if len(driver.find_elements(By.CSS_SELECTOR,'li.filter-block a.js-search-link i')) ==0:
            logging.info("Test pass: All filter closed")
        else:
            logging.error(f"Test fail: {len(driver.find_elements(By.CSS_SELECTOR,'li.filter-block a.js-search-link i'))} didn't close")
    except:
        logging.error("Test fail: Filter didn't close")

def testcase_5():
    visit_website()
    filter(0)
    filter(1)
    filter(2)
    clear_each_filter(3)

if __name__ == "__main__":
    testcase_5()