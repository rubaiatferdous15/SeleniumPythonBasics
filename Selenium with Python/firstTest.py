from selenium import webdriver


browser = webdriver.Chrome()
browser.get("https://www.selenium.dev/")
browser.maximize_window()
title = browser.title
print(title)
assert "Selenium" in title