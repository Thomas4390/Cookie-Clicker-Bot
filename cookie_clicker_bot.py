#!/usr/local/bin/python3
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(
    '/Users/thomasvaudescal/Documents/Mes_documents/22_VSCODE/Cookie-Clicker-Bot/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://www.google.com/')

time.sleep(5)
driver.quit()