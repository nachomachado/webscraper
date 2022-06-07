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
    
    notes_tab = driver.find_element_by_xpath('//a[contains(@href,"#tab_notas")]')
    notes_tab.click()
    notes_table = driver.find_element_by_xpath('//*[@id="tab_notas"]/div/table/tbody')
    for row in notes_table.find_elements_by_tag_name('tr'):
        for element in row.find_elements_by_tag_name('td'):
            print(element.text)

    driver.quit()

if __name__ == '__main__':
    run()