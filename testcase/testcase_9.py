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
logging.basicConfig(filename='./logs/testcase_9.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
website_url = "http://teststore.automationtesting.co.uk/6-accessories"

def float_value(s):
    return float(s[1:])


def visit_website():
    driver.get(website_url)



def filter():
    filters = driver.find_elements(By.CSS_SELECTOR,"label.facet-label a")
    for filter in filters:
        if "Home Accessories" in filter.text:
            matches = re.findall(r'\d+', filter.text)
            filter.click()
            logging.info("Test pass: Filtered")
            time.sleep(3)
            if matches:
                return int(matches[0])
    logging.error("Test fail: There's no Home Accessories Filter")


def check_filter_active():
    try:
        fileter_active = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.CSS_SELECTOR,"section.active_filters ul li")))
        return True
    except:
        return False

def get_total_product():
    total_element = driver.find_element(By.CSS_SELECTOR,"div.total-products p")
    matches = re.findall(r'\d+', total_element.text)

    if matches:
        return int(matches[0])
    
def clear_all():
    clear_button = driver.find_element(By.CSS_SELECTOR,"button.js-search-filters-clear-all")
    clear_button.click()
    time.sleep(2)

def testcase_9():
    visit_website()
    filter()
    if check_filter_active():
        logging.info("Test pass: Filter active worked")
    else:
        logging.error("Test fail: Filter active didn't work")

    clear_all()

    if check_filter_active():
        logging.error("Test fall: Clear all didn't work")
    else:
        logging.info("Test pass: Clear all worked")
    

    

if __name__ == "__main__":
    testcase_9()