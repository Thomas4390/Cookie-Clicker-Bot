#!/usr/local/bin/python3
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = '/Users/thomasvaudescal/Documents/Mes_documents/22_VSCODE/Cookie-Clicker-Bot/chromedriver'

service = Service(path)
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://orteil.dashnet.org/cookieclicker/v10466/')

time.sleep(1000)

driver.find_element_by_id('bigCookie').click()

driver.quit()