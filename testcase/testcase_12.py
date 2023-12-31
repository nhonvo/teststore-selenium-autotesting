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
logging.basicConfig(filename='./logs/testcase_12.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
action = ActionChains(driver)
website_url = "http://teststore.automationtesting.co.uk"
first_product = 1
second_product = 2
def float_value(s):
    return float(s[1:])


def visit_website():
    driver.get(website_url)


def check_quickview(number):
 
    product_element = driver.find_elements(By.CLASS_NAME,"product-thumbnail")
    chosend_element = product_element[number]
    
    action.move_to_element(chosend_element).perform()
    quick_view = driver.find_elements(By.CSS_SELECTOR,'a.quick-view')
    try:
        quick_view[number].click()
    except:
        logging.error("Test fail: Quickview didn't open")

    time.sleep(2)
    modal = driver.find_elements(By.CLASS_NAME,'modal-dialog-centered')
    if len(modal) == 0:
        logging.error("Test fail: Quickview didn't open")
        return
    logging.info("Test pass: Quickview work")

    try:
        cart_button = driver.find_element(By.CSS_SELECTOR,'div.product-quantity div.add button.add-to-cart')
    
        cart_button.click()
        time.sleep(5)
        cart = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.CSS_SELECTOR,"h4.modal-title")))
        if 'Product successfully added to your shopping cart' in cart.text:
            logging.info("Test pass: Cart opened")
        else:
            logging.error("Test fail: Cart didn't open")

    except:
        logging.error("Test fail: Cart didn't open")
        return
    time.sleep(3)
    close_button = driver.find_element(By.CSS_SELECTOR,'button.close')
    close_button.click()
    time.sleep(3)

def check_cart(number):
    cart_button = driver.find_element(By.CLASS_NAME,"cart-products-count")
    cart_button.click()
    time.sleep(3)
    try:
        cart_div = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"cart-container")))
        input_amount = driver.find_elements(By.CLASS_NAME,"js-cart-line-product-quantity")
        if len(input_amount)==number:
            logging.info(f"Test pass: Cart have {number} products")
        else:
            logging.error(f"Test fail: Cart have {len(input_amount)} products")
    except:
        logging.error("Test fail: Cart page didn't open")


def testcase_12():
    visit_website()
    check_quickview(0)
    check_quickview(0)
    check_cart(1)
    visit_website()
    check_quickview(1)
    check_cart(2)

    
    
    

    

if __name__ == "__main__":
    testcase_12()