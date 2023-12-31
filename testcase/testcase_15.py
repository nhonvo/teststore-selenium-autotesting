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
logging.basicConfig(filename='./logs/testcase_15.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
action = ActionChains(driver)
website_url = "http://teststore.automationtesting.co.uk/prices-drop"
first_product = 1
second_product = 2
def float_value(s):
    return float(s[1:])


def visit_website():
    driver.get(website_url)

def check_sales():
    products = driver.find_elements(By.CSS_SELECTOR,"article.product-miniature")
    sales = driver.find_elements(By.CSS_SELECTOR,"ul.product-flags li.discount")
    if(len(products)==len(sales)):
        logging.info("Tess pass: All product have discount")
    else:
        logging.error(f"Test fail: {len(sales)}/{len(products)} product have discount")

def testcase_15():
    visit_website()
    check_sales()
    
    
    

    

if __name__ == "__main__":
    testcase_15()