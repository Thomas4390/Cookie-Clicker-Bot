from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()

chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('detach', True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
driver.maximize_window()
driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

driver.implicitly_wait(10)
sum1 = driver.find_element(By.ID, 'sum1').send_keys('10')

driver.find_element(By.ID, 'at-cv-lightbox-close').click()
#sum2 = driver.find_element(By.ID, 'sum2').send_keys('20')
#total = driver.find_element(By.ID, 'gettotal').click()

