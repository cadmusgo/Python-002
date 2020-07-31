"""
1. pip intall selenium
2. copy chromedriver.exe to venv\Scripts
"""
from selenium import webdriver
import time

user_name = 'fake_email@email.com'
password = '1231312312312321'

browser = webdriver.Chrome()
browser.get('https://shimo.im/login?from=home')

time.sleep(1)

elEmail = browser.find_element_by_name("mobileOrEmail")
elPassword = browser.find_element_by_name("password")

elEmail.send_keys(user_name)
elPassword.send_keys(password)

btnSubmit = browser.find_elements_by_tag_name("button")[0]
btnSubmit.click()
