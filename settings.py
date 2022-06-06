
import platform
from dotenv import load_dotenv #environment variables
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_settings():
    '''
    Return settings variables read from the .env file to the main script in the next format:
    URL, USER, PASSWORD, WAITING_TIME, driver
    The driver is already set to be used.
    '''
    PATHS = {
        'Windows':'./drivers/chromedriver.exe',
        'Darwin':'./drivers/chromedriver',
        'Linux':'./drivers/chromedriverlinux'
        }
    try:
        DRIVER_PATH = PATHS[platform.system()]
    except IndexError:
        print('This progam do not work in this device.')

    load_dotenv()
    data = ['WORKSHOP', 'USER', 'PASSWORD','WAITING_TIME']
    URL, USER, PASSWORD, WAITING_TIME = map(os.getenv, data)

    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(DRIVER_PATH) 
    
    return URL, USER, PASSWORD, int(WAITING_TIME), driver

def run():
    print('This module runs from script sel_webscraper.py. From terminal execute  "python3 sel_webscraper.py" ')

if __name__ == '__main__':
    run()
