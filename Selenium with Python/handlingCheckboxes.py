import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://fs2.formsite.com/USrSn6/yxndcqj3zv/index?fbclid=IwY2xjawL1r65leHRuA2FlbQIxMABicmlkETFydGp5a01haDFnc3FFb2Z5AR66Eo1APW2On8vrlOp0fFoa6MTloejB7-_RlouxUAOwSgXLfmak5J_C0-Apzg_aem_KBBnPB50wFud6rw93AnZyw')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.XPATH, "//label[normalize-space()='Fund Raising']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//label[normalize-space()='Fund Raising']").click()
time.sleep(2)
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)
    time.sleep(2)
checked_count = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count+=1


expected_count = 17

if checked_count == expected_count:
    print('verified')
else:
    print('failed')
time.sleep(3)
driver.close()