import time
from selenium import webdriver
from login import autologin
from settings import get_settings
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run():
    '''
    Run script
    '''
    URL, USER, PASSWORD, WAITING_TIME, driver = get_settings()
    driver = autologin(driver, URL, USER, PASSWORD)
    time.sleep(WAITING_TIME)
    
    driver.get('https://taller.gestioo.net/taller/ordenes/sucursal/259#a_1')
    
    time.sleep(WAITING_TIME)

    ot = pd.read_excel('ot.xlsx', header=1)

    notas = {}

    timeout = 2.5

    for n in ot['ORDEN N°']:
        zoom = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="appVue"]/div/div[1]/div/div/div[2]/div/button[2]/i')))
        zoom = driver.find_element_by_xpath('//*[@id="appVue"]/div/div[1]/div/div/div[2]/div/button[2]/i')
        zoom.click()
        
        box = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="f_busqueda_orden_div"]/input[1]')))
        box = driver.find_element_by_xpath('//*[@id="f_busqueda_orden_div"]/input[1]')
        box.click()
        box.send_keys(int(n))
        box.send_keys(Keys.ENTER)
        
        tab = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal_busqueda_orden"]/div/div/div[2]/div[4]/div/div/ul/li[2]/a')))
        tab = driver.find_element_by_xpath('//*[@id="modal_busqueda_orden"]/div/div/div[2]/div[4]/div/div/ul/li[2]/a')
        tab.click()
        
        try: 
            time.sleep(0.5)
            note = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal_orden_tabla_notas"]')))
            note = driver.find_element_by_xpath('//*[@id="modal_orden_tabla_notas"]')
            print(n,':',note.text)
        except:
            try:
                note = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal_orden_sin_notas"]')))
                note = driver.find_element_by_xpath('//*[@id="modal_orden_sin_notas"]').text
                print(n,':',note)   
            except:
                print('ERROR CON EL ELEMENTO NOTAS')
                driver.close()

        close = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal_busqueda_orden"]/div/div/div[1]/button')))
        close = driver.find_element_by_xpath('//*[@id="modal_busqueda_orden"]/div/div/div[1]/button')
        close.click()

    output = pd.DataFrame(data = notas, columns=['OT', 'NOTAS TECNICAS'])
    output.to_csv('notas.csv')
    driver.quit()

if __name__ == '__main__':
    run()