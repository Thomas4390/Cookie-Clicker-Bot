#!/usr/local/bin/python3
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

service = Service(ChromeDriverManager().install())

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

driver.maximize_window()

driver.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(3)
#<div class="langSelectButton title" style="padding:4px;" id="langSelect-FR">Français</div>
langage_menu = driver.find_element(By.ID, 'langSelect-FR')
driver.implicitly_wait(10)
langage_menu.click()

