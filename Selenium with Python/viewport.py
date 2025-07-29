import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.google.com/")
viewports = [(1024,768),(768,1024),(375,667)]
driver.set_window_size(768,1024)
time.sleep(5)


try:
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(5)
finally:
    driver.close()