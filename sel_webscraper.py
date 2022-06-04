from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv #environment variables
import platform


 




def autologin(driver, url, username, password):
   
    """
    Login at site with url, username and password passed.
    """
    #  Open website
    driver.get(url)
    # Find a password input field and enter the specified password string
    password_input = driver.find_element(by=By.XPATH, value="//input[@type='password']")
    password_input.send_keys(password)
    # Find a visible input field preceding out password field and enter the specified username
    username_input = password_input.find_element(by=By.XPATH, value=".//preceding::input[not(@type='hidden')]")
    username_input.send_keys(username)
    # Find the form element enclosing our password field
    form_element = password_input.find_element(by=By.XPATH, value=".//ancestor::form")
    # Find the form's submit element and click it
    submit_button = form_element.find_element(by=By.XPATH, value=".//*[@type='submit']")
    submit_button.click()

    return driver

def run():
    '''
    Run script
    '''
    load_dotenv()
    if(platform.system() == "Windows"):
        DRIVER_PATH = './chromedriver.exe'
        print('open chrome on windows')
    elif(platform.system ==macOS):
        DRIVER_PATH = './chromedriver'
    URL = os.getenv('WORKSHOP')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    WAITING_TIME = 15
    
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(DRIVER_PATH) 
    driver = autologin(driver, URL, USER, PASSWORD)
    time.sleep(WAITING_TIME) 
    driver.quit()



if __name__ == '__main__':
    run()
