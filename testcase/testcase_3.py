from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(filename='./logs/testcase_3.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
website_url = "http://teststore.automationtesting.co.uk/3-clothes"


def float_value(s):
    return float(s[1:])


def visit_website():
    driver.get(website_url)

def filter():
    dropdown_button = driver.find_element(By.CSS_SELECTOR,"div.products-sort-order button")
    dropdown_button.click()
    filter_list = driver.find_elements(By.CSS_SELECTOR,"div.dropdown-menu a")
    for filter in filter_list:
        if 'Price, low to high' in filter.text:
            filter.click()
    time.sleep(2)

    if driver.current_url == "http://teststore.automationtesting.co.uk/3-clothes?order=product.price.asc":
        logging.info("Test pass: Filter successed")
    else:
        logging.error("Test fail: Filter fail")


def verify_order_product():
    list_price=driver.find_elements(By.CSS_SELECTOR,"div.product-price-and-shipping span.price")
    is_asc = True
    for i in range(1,len(list_price)):
        is_asc &= float_value(list_price[i-1].text) <= float_value(list_price[i].text)

    if is_asc:
        logging.info(f"Test pass: The products have been sorted ascending")
    else:
        logging.error(f"Test fail: The products haven't been sorted ascending")

def testcase_3():
    visit_website()
    filter()
    verify_order_product()

if __name__ == "__main__":
    testcase_3()