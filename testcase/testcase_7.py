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
logging.basicConfig(filename='./logs/testcase_7.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
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

def get_total_product():
    total_element = driver.find_element(By.CSS_SELECTOR,"div.total-products p")
    matches = re.findall(r'\d+', total_element.text)

    if matches:
        return int(matches[0])


def verify_number_of_product(require, total):
    list_product=driver.find_elements(By.CSS_SELECTOR,"article.product-miniature")
    if require==total and total == len(list_product):
        logging.info(f"Test pass: The page already displays all products")
    else:
        logging.error(f"Test fail: The number of products displayed is incorrect")

def sort_asc():
    dropdown_button = driver.find_element(By.CSS_SELECTOR,"div.products-sort-order button")
    dropdown_button.click()
    filter_list = driver.find_elements(By.CSS_SELECTOR,"div.dropdown-menu a")
    for filter in filter_list:
        if 'Price, low to high' in filter.text:
            filter.click()
    time.sleep(2)
    # driver.implicitly_wait(4)
    if driver.current_url == "http://teststore.automationtesting.co.uk/6-accessories?q=Categories-Home+Accessories&order=product.price.asc":
        logging.info("Test pass: Sort successed")
    else:
        logging.error("Test fail: Sort fail")


def verify_order_product():
    list_price=driver.find_elements(By.CSS_SELECTOR,"div.product-price-and-shipping span.price")
    is_asc = True
    for i in range(1,len(list_price)):
        is_asc &= float_value(list_price[i-1].text) <= float_value(list_price[i].text)

    if is_asc:
        logging.info(f"Test pass: The products have been sorted ascending")
    else:
        logging.error(f"Test fail: The products haven't been sorted ascending")

def testcase_7():
    visit_website()
    verify_number_of_product(filter(),get_total_product())
    sort_asc()
    verify_order_product()

if __name__ == "__main__":
    testcase_7()