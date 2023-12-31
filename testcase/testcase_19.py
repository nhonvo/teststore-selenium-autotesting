from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait,Select
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
logging.basicConfig(filename='./logs/testcase_19.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
action = ActionChains(driver)
website_url = "http://teststore.automationtesting.co.uk"
number = 1
def float_value(s):
    return float(s[1:])


def visit_website():
    driver.get(website_url)


def go_to_login_page():
    signin_button = driver.find_element(By.CSS_SELECTOR,'div.user-info a')
    signin_button.click()

def submit_with_valid_info():
    try:
        wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"email")))
    except:
        logging.error("The login page cannot be opened")
    email_input = driver.find_element(By.NAME,"email")
    password_input = driver.find_element(By.NAME,"password")
    submit_button = driver.find_element(By.ID, 'submit-login')
    email_input.clear()
    password_input.clear()
    email_input.send_keys(os.getenv("VALID_EMAIL"))
    password_input.send_keys(os.getenv("CORRECT_PASSWORD"))
    submit_button.submit()
    try:
        logout_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.user-info a.logout")))
        logging.info("Test pass: Logged in")
    except:
        logging.error("Test fail: Loggin failed")

def change_address():
    info_button = driver.find_elements(By.CSS_SELECTOR,'span.link-item')[1]
    info_button.click()
    wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"address-body")))

    driver.find_elements(By.CSS_SELECTOR,'div.address-footer a')[0].click()

    wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"address1")))

    address = driver.find_element(By.NAME,"address1")
    address.clear()
    address.send_keys("TP.HCMMMMM")
    city = driver.find_element(By.NAME,'city')
    city.clear()
    city.send_keys('TP.HCMMMM')
    postcode = driver.find_element(By.NAME,'postcode')
    postcode.clear()
    postcode.send_keys("12312")
    select = driver.find_element(By.TAG_NAME,'select')
    select.click()
    # time.sleep(2)
    options = driver.find_elements(By.TAG_NAME,'option')
    options[3].click()
    out_option = driver.find_element(By.CSS_SELECTOR,'div div div.form-control-comment')
    out_option.click()
    time.sleep(3)

    
    continue_button = driver.find_element(By.CSS_SELECTOR,'footer.form-footer button')
    continue_button.click()
    time.sleep(2)


def check_changes():
    driver.get("http://teststore.automationtesting.co.uk/address?id_address=10246") 
    # time.sleep(10000)


    address1 = driver.find_element(By.NAME,'address1')
    # print(address1.get_attribute('value'))
    if address1.get_attribute("value") != "TP.HCMMMMM":
        logging.error("Test fail: Didn't change address")
        return

    city = driver.find_element(By.NAME,'city')
    if city.get_attribute("value") != "TP.HCMMMM":
        logging.error("Test fail: Didn't change address")
        return

    postcode = driver.find_element(By.NAME,'postcode')
    if postcode.get_attribute("value") != "12312":
        logging.error("Test fail: Didn't change address")
    select_element = driver.find_element(By.TAG_NAME,'select')
    select = Select(select_element)
    options = select.options
    for option in options:
        if option.is_selected():
            if option.get_attribute("value")!='3':
                logging.error("Test fail: Didn't change address")
    
    logging.info("Tess pass: Address changed")
def testcase_19():
    visit_website()
    go_to_login_page()
    submit_with_valid_info()
    change_address()
    check_changes()
    
    

    

if __name__ == "__main__":
    testcase_19()