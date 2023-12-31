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
logging.basicConfig(filename='./logs/testcase_2.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
website_url = "http://teststore.automationtesting.co.uk/"



def visit_website():
    driver.get(website_url)

def search():
    search_input = driver.find_element(By.NAME,"s")
    search_button = driver.find_element(By.CSS_SELECTOR,"i.search")

    search_input.send_keys(os.getenv("SEARCH_KEY"))
    search_button.click()

    driver.implicitly_wait(1)
    if driver.current_url == "http://teststore.automationtesting.co.uk/search?controller=search&s=HUMMINGBIRD+PRINTED":
        logging.info("Test pass: Search successed")
    else:
        logging.error("Test fail: Search fail")


def verify_name_product():
    list_product=driver.find_elements(By.CSS_SELECTOR,"h2.product-title a")
    count = 0
    for product in list_product:
        if os.getenv('SEARCH_KEY').lower() in product.text.lower() :
            count +=1
    if count == len(list_product):
        logging.info(f"Test pass: {count}/{count} products contain the key")
    else:
        logging.error(f"Test fail: {len(list_product)-count}/{len(list_product)} products don't contain the key")

def testcase_2():
    visit_website()
    search()
    verify_name_product()

if __name__ == "__main__":
    testcase_2()