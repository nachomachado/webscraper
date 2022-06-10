from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def goto_home(driver):
    driver.get('https://taller.gestioo.net/taller/ordenes/sucursal/259#a_1')
    return

def show_ot(n, driver, timeout=5):
    zoom = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="appVue"]/div/div[1]/div/div/div[2]/div/button[2]/i')))
    zoom = driver.find_element_by_xpath('//*[@id="appVue"]/div/div[1]/div/div/div[2]/div/button[2]/i')
    zoom.click()
        
    box = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="f_busqueda_orden_div"]/input[1]')))
    box = driver.find_element_by_xpath('//*[@id="f_busqueda_orden_div"]/input[1]')
    box.click()
    box.send_keys(int(n))
    box.send_keys(Keys.ENTER)   
    return

def close_ot(driver, timeout=5):
    close = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal_busqueda_orden"]/div/div/div[1]/button')))
    close = driver.find_element_by_xpath('//*[@id="modal_busqueda_orden"]/div/div/div[1]/button')
    close.click()
    return 

def get_notes(driver, timeout=5):
    tab = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal_busqueda_orden"]/div/div/div[2]/div[4]/div/div/ul/li[2]/a')))
    tab = driver.find_element_by_xpath('//*[@id="modal_busqueda_orden"]/div/div/div[2]/div[4]/div/div/ul/li[2]/a')
    tab.click()
        
    try: 
        time.sleep(0.5)
        note = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal_orden_tabla_notas"]')))
        note = driver.find_element_by_xpath('//*[@id="modal_orden_tabla_notas"]')
    except:
        try:
            note = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal_orden_sin_notas"]')))
            note = driver.find_element_by_xpath('//*[@id="modal_orden_sin_notas"]')
        except:
            print('ERROR CON EL ELEMENTO NOTAS')
            driver.close()
        
    return note.text



def get_pys():
    return


if __name__ == '__main__':
    print('This module has the functions that allow you to get the information from each OT. It has to be called from another script.')