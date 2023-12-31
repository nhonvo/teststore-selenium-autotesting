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
logging.basicConfig(filename='./logs/testcase_4.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
website_url = "http://teststore.automationtesting.co.uk/"



def visit_website():
    driver.get(website_url)

def search():
    search_input = driver.find_element(By.NAME,"s")
    search_button = driver.find_element(By.CSS_SELECTOR,"i.search")

    search_input.send_keys(os.getenv("NO_PRODUCT_SEARCH_KEY"))
    search_button.click()

    driver.implicitly_wait(1)
    if driver.current_url == "http://teststore.automationtesting.co.uk/search?controller=search&s=nhon+dep+trai":
        logging.info("Test pass: Search successed")
    else:
        logging.error("Test fail: Search fail")


def verify_product():
    try:
        not_found_text = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"section.page-not-found h4")))
        if not_found_text.text == "Sorry for the inconvenience.":
            logging.info("Test pass: Provided the text apology")
    except:
        logging.error("Test fail: There are still products for the keyword that do not exist")

def testcase_4():
    visit_website()
    search()
    verify_product()

if __name__ == "__main__":
    testcase_4()