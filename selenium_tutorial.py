#!/usr/local/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')
print(driver.title)
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)

download_button = driver.find_element(By.ID, 'downloadButton')
download_button.click()

progress_element = driver.find_element(By.CLASS_NAME, 'progress-label')
print()



simple_form = driver.find_element(By.LINK_TEXT, 'Input Forms')
simple_form.click()
driver.implicitly_wait(10)
simple_form_demo = driver.find_element(By.LINK_TEXT, 'Input Forms Demo')
simple_form_demo.click()

time.sleep(100)









