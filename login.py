from selenium import webdriver
from selenium.webdriver.common.by import By


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