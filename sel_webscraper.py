import time
from selenium import webdriver
from login import autologin
from settings import get_settings
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ot_functions as otf


def run():
    '''
    Run script
    '''
    URL, USER, PASSWORD, WAITING_TIME, driver = get_settings()
    timeout = 2.5
    driver = autologin(driver, URL, USER, PASSWORD)

    time.sleep(WAITING_TIME)   
    otf.goto_home(driver)
    time.sleep(WAITING_TIME)

    ot = set(pd.read_excel('ot.xlsx', header=1)['ORDEN N°'])
    saved = set(pd.read_csv('notas.csv', index_col=0).index)

    for n in ot-saved:

        otf.show_ot(n, driver, timeout=timeout)    
        notas= otf.get_notes(driver, timeout=timeout)
        otf.close_ot(driver, timeout=timeout)
        pd.DataFrame(data=[notas], index = [n]).to_csv('notas.csv', header=False, mode='a')

    driver.quit()

if __name__ == '__main__':
    run()