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
logging.basicConfig(filename='./logs/testcase_23.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
action = ActionChains(driver)
total_product = 0
def float_value(s):
    return float(s[1:])


def visit_website(website_url="http://teststore.automationtesting.co.uk"):
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

def check_contact():
    driver.find_element(By.CSS_SELECTOR,'div#contact-link a').click()
    try:
        wait_load = WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.CSS_SELECTOR,"section.contact-form")))
    except:
        logging.error("Test fail: Fail to load contact page")
    logging.info("Test pass: Success to load contact page")
    subject_select_element = driver.find_element(By.NAME,'id_contact')
    subject_select = Select(subject_select_element)
    subject_select.select_by_index(random.randint(0,1))
    
    order_ref_element = driver.find_element(By.NAME,'id_order')
    order_ref = Select(order_ref_element)
    order_ref.select_by_index(random.randint(1,4))

    
    message_element = driver.find_element(By.NAME,'message')
    message_element.send_keys("HELP ME!!!")


    check_box = driver.find_element(By.ID,'psgdpr_consent_checkbox_1')
    check_box.click()
    submit_button = driver.find_element(By.NAME,'submitMessage')
    submit_button.click()
    try:
        wait_load = WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.alert-success")))
        logging.info("Test pass: Send email success")
    except:
        logging.error("Test fail: Send email fail")
    

    
def testcase_23():
    visit_website()
    go_to_login_page()
    submit_with_valid_info()
    check_contact()
    
    
    

    

if __name__ == "__main__":
    testcase_23()