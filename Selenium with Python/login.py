from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.maximize_window()


username = "standard_user"
password = "secret_sauce"

login_url = "https://www.saucedemo.com/"

browser.get(login_url)

username_field = browser.find_element(By.ID,"user-name")
password_field = browser.find_element(By.ID,"password")


username_field.send_keys(username)
password_field.send_keys(password)

login_button = browser.find_element(By.ID,"login-button")

assert not login_button.get_attribute("disabled")

login_button.click()


success_element = browser.find_element(By.CSS_SELECTOR,".title")

assert success_element.text == "Products"