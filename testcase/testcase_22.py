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
logging.basicConfig(filename='./logs/testcase_22.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
action = ActionChains(driver)
total_product = 0
def float_value(s):
    return float(s[1:])


def visit_website(website_url="http://teststore.automationtesting.co.uk/2-home"):
    driver.get(website_url)

def get_total_product():
    total_element = driver.find_element(By.CSS_SELECTOR,"div.total-products p")
    matches = re.findall(r'\d+', total_element.text)

    if matches:
        return int(matches[0])
    
def testcase_22():
    visit_website()
    total_product = get_total_product()
    count = 0
    while True:
        count += len(driver.find_elements(By.CSS_SELECTOR,"article.product-miniature"))
        try:
            driver.find_element(By.CSS_SELECTOR,'a.next').click()
            time.sleep(2)
        except:
            break 
    if count == total_product:
        logging.info("Test pass: The page already displays all products")
    else:
        logging.error(f"Test fail: The number of products displayed is incorrect")
    
    
    

    

if __name__ == "__main__":
    testcase_22()