#!/usr/local/bin/python3
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(3)
#<div class="langSelectButton title" style="padding:4px;" id="langSelect-FR">Français</div>
langage_menu = driver.find_element(By.ID, 'langSelect-FR')
driver.implicitly_wait(10)
langage_menu.click()

