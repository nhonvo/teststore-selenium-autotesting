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
logging.basicConfig(filename='./logs/testcase_24.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
action = ActionChains(driver)
total_product = 0
def float_value(s):
    return float(s[1:])


def visit_website(website_url="http://teststore.automationtesting.co.uk"):
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
        print("there")
    
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
    filters[0].click()
    time.sleep(3)

def check_cart():
    cart_button = driver.find_element(By.CLASS_NAME,"cart-products-count")
    cart_button.click()
    time.sleep(3)
    global total
    
    try:
        cart_div = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"cart-container")))
    except:
        logging.error("Test fail: Cart page didn't open")


def fill_person_info():
    checkout_button = driver.find_element(By.CSS_SELECTOR,"div.checkout div a")
    checkout_button.click()
    order_page = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"checkout-personal-information-step")))
    id_gender = driver.find_elements(By.NAME,'id_gender')
    id_gender[0].click()
    first_name = driver.find_element(By.NAME,"firstname")
    first_name.send_keys("firstname")
    # time.sleep(1000)
    last_name = driver.find_element(By.NAME,"lastname")
    last_name.send_keys("lastname")
    # time.sleep(1000)
    last_name = driver.find_element(By.NAME,"email")
    last_name.send_keys("email@email.com")
    # time.sleep(1000)
    check_box = driver.find_element(By.NAME,'psgdpr')
    check_box.click()

    continue_button = driver.find_element(By.NAME,"continue")
    continue_button.click()

    wait_load = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"checkout-addresses-step")))
    address = driver.find_element(By.NAME,"address1")
    address.send_keys("TP.HCM")
    city = driver.find_element(By.NAME,'city')
    city.send_keys('TP.HCM')
    postcode = driver.find_element(By.NAME,'postcode')
    postcode.send_keys("12345")
    select = driver.find_element(By.TAG_NAME,'select')
    select.click()
    options = driver.find_elements(By.TAG_NAME,'option')
    options[2].click()
    continue_button = driver.find_element(By.NAME,'confirm-addresses')
    continue_button.click()
    wait_load = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"confirmDeliveryOption")))

    continue_button = driver.find_element(By.NAME,'confirmDeliveryOption')
    continue_button.click()
    wait_load = WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input.ps-shown-by-js")))
    pay_checkbox = driver.find_elements(By.CSS_SELECTOR,"input.ps-shown-by-js")[1]
    pay_checkbox.click()
    check_box = driver.find_element(By.ID,'conditions_to_approve[terms-and-conditions]')
    check_box.click()
    continue_button = driver.find_element(By.CSS_SELECTOR,'div#payment-confirmation div button')
    continue_button.click()
    try:
        wait_load = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"tr.total-value")))
        logging.info('Test pass: Ordered')
    except:
        logging.error('Test fail: Order failed')

def testcase_24():
    visit_website('http://teststore.automationtesting.co.uk/2-home')
    driver.find_element(By.CSS_SELECTOR,'a.next').click()
    wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"a.previous")))
    check_quickview(1)
    filter()
    check_quickview(-2)
    check_cart()
    fill_person_info()

    
    
    

    

if __name__ == "__main__":
    testcase_24()