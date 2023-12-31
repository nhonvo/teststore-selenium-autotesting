from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()
import logging
logging.basicConfig(filename='./logs/testcase_1.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
website_url = "http://teststore.automationtesting.co.uk/"
def visit_website():
    driver.get(website_url)

def go_to_login_page():
    signin_button = driver.find_element(By.CSS_SELECTOR,'div.user-info a')
    signin_button.click()

def submit_with_invalid_info():
    try:
        email_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"email")))
    except:
        logging.error("The login page cannot be opened")
    email_input = driver.find_element(By.NAME,"email")
    password_input = driver.find_element(By.NAME,"password")
    submit_button = driver.find_element(By.ID, 'submit-login')

    email_input.send_keys(os.getenv("INVALID_EMAIL"))
    password_input.send_keys(os.getenv("INCORRECT_PASSWORD"))
    submit_button.submit()

    try:
        authen_alert = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"ul li.alert")))
    except:
        logging.error("The page does not report login error")

    authen_alert = driver.find_element(By.CSS_SELECTOR,"ul li.alert")

    if authen_alert.text == "Authentication failed.":
        logging.info("Test pass: Login failed")
    else:
        logging.error("Test fail: Do not display incorrect login information")

    if driver.current_url == "http://teststore.automationtesting.co.uk/login?back=my-account":
        logging.info("Test pass: Still in login page")
    else:
        logging.error("No longer on the login page")
        driver.get("http://teststore.automationtesting.co.uk/login?back=my-account")
    
def submit_with_valid_info():
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

    if driver.current_url == "http://teststore.automationtesting.co.uk/my-account":
        logging.info("Test pass: Redirect to My account page")
    else:
        logging.error("Test fail: Doesn't redirect to My account page")
    
def logout():
    logout_button = driver.find_element(By.CSS_SELECTOR,"div.user-info a.logout")
    logout_button.click()

    try:
        signin_text = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.user-info a span')))
        if signin_text.text == "Sign in":
            logging.info("Test pass: Logged out")
        else:
            logging.error("Test fail: Logout failed")
    except:
        logging.error("Test fail: Logout failed")



def testcase_1():
    
    visit_website()
    
    go_to_login_page()
    
    submit_with_invalid_info()
    
    submit_with_valid_info()

    logout()
    

    driver.quit()
        



if __name__ == "__main__":
    testcase_1()



