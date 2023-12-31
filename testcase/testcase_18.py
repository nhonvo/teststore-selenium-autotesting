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
logging.basicConfig(filename='./logs/testcase_18.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
action = ActionChains(driver)
website_url = "http://teststore.automationtesting.co.uk"
total = 0
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

def change_info():
    info_button = driver.find_elements(By.CSS_SELECTOR,'span.link-item')[0]
    info_button.click()
    wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"firstname")))
    firstname = driver.find_element(By.NAME,'firstname')
    firstname.clear()
    firstname.send_keys("Nhon")
    password = driver.find_element(By.NAME,'password')
    password.send_keys(os.getenv("CORRECT_PASSWORD"))
    check_box = driver.find_element(By.NAME,'psgdpr')
    check_box.click()
    time.sleep(2)
    submit_button = driver.find_element(By.CSS_SELECTOR,'button.form-control-submit')
    submit_button.click()
    time.sleep(2)

def check_changes():
    driver.get("http://teststore.automationtesting.co.uk/identity") 
    time.sleep(2)
    firstname = driver.find_element(By.NAME,'firstname')
    if firstname.get_attribute("value") == "Nhon":
        logging.info("Test pass: Changed info")
    else:
        logging.error("Test fail: Didn't change info")
    
def testcase_18():
    visit_website()
    go_to_login_page()
    submit_with_valid_info()
    change_info()
    check_changes()
    
    

    

if __name__ == "__main__":
    testcase_18()