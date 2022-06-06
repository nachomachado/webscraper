import time
from selenium import webdriver
from login import autologin
from settings import get_settings

def run():
    '''
    Run script
    '''
    URL, USER, PASSWORD, WAITING_TIME, driver = get_settings()
    driver = autologin(driver, URL, USER, PASSWORD)
    time.sleep(WAITING_TIME)
    driver.get('https://taller.gestioo.net/taller/ordenes/sucursal/259#28018')
    time.sleep(2)
    driver.quit()

if __name__ == '__main__':
    run()
