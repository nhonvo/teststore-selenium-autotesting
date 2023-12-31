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
logging.basicConfig(filename='./logs/testcase_25.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
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


def click_nav():
    driver.find_elements(By.CSS_SELECTOR,'div.menu ul#top-menu li a')[0].click()
    try:
        wait = WebDriverWait(driver,10).until((EC.presence_of_element_located((By.CSS_SELECTOR,"js-product-list-header"))))
        logging.info('Test pass: Nav worked')
    except:
        logging.error("Test fail: Nav didn't work")

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
    

    input_color = driver.find_elements(By.CLASS_NAME,"input-color")
    

    if len(input_color)!=0:
        number = random.randint(0,len(input_color)-1)
        input_color[number].click()
        time.sleep(1)
        chosen = driver.find_element(By.CSS_SELECTOR,'span.color span.sr-only')
        # #print(chosen)
        type = chosen.text
    selector = driver.find_elements(By.TAG_NAME,"select")
    if len(selector)!=0:
        


        selector[0].click()
        time.sleep(2)
        option_sizes = driver.find_elements(By.TAG_NAME,"option")   
        number = random.randint(0,len(option_sizes)-1)
        size = option_sizes[number].text


        option_sizes[number].click()
        time.sleep(2)
    
    button_up = driver.find_element(By.CSS_SELECTOR,"button.bootstrap-touchspin-up")
    count = random.randint(1,10)
    for _ in range(count-1):
        button_up.click()


    try:
        cart_button = driver.find_element(By.CSS_SELECTOR,'div.product-quantity div.add button.add-to-cart')
    
        cart_button.click()
        time.sleep(2)
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




def filter():
    filters = driver.find_elements(By.CSS_SELECTOR,"label.facet-label a")
    filters[3].click()
    time.sleep(3)

def check_cart():
    cart_button = driver.find_element(By.CLASS_NAME,"cart-products-count")
    cart_button.click()
    time.sleep(3)
    global total
    total = float_value(driver.find_element(By.CSS_SELECTOR,"div.cart-total span.value").text)

    try:
        cart_div = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"cart-container")))
    except:
        logging.error("Test fail: Cart page didn't open")


def complete_order():
    checkout_button = driver.find_element(By.CSS_SELECTOR,"div.checkout div a")
    checkout_button.click()
    wait_load = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"checkout-personal-information-step")))

    address_list = driver.find_elements(By.NAME,'id_address_delivery')
    address_list[random.randint(0,6)].click()
    continue_button = driver.find_element(By.NAME,'confirm-addresses')
    continue_button.click()
    wait_load = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"confirmDeliveryOption")))

    continue_button = driver.find_element(By.NAME,'confirmDeliveryOption')
    continue_button.click()
    wait_load = WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.ps-shown-by-js")))

    pay_checkbox = driver.find_elements(By.CSS_SELECTOR,"input.ps-shown-by-js")[0]
    pay_checkbox.click()

    check_box = driver.find_element(By.ID,'conditions_to_approve[terms-and-conditions]')
    check_box.click()
    continue_button = driver.find_element(By.CSS_SELECTOR,'div#payment-confirmation div button')
    continue_button.click()
    wait_load = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"tr.total-value")))


def testcase_25():
    visit_website()
    go_to_login_page()
    submit_with_valid_info()
    click_nav()
    check_quickview(0)
    filter()
    check_quickview(-1)
    check_cart()
    complete_order()



if __name__ == "__main__":
    testcase_25()