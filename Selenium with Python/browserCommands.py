import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()


browser.get("https://opensource-demo.orangehrmlive.com")
browser.maximize_window()
browser.minimize_window()
browser.fullscreen_window()
time.sleep(5)
browser.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(5)
browser.back()
time.sleep(5)
browser.forward()
time.sleep(5)
browser.refresh()
browser.close()
