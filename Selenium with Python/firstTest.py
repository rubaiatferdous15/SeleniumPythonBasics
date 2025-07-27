from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("https://www.selenium.dev/")
browser.maximize_window()
title = browser.title
print(title)
assert "Selenium" in title

browser.find_element(By.CSS_SELECTOR,"Getting Started")
