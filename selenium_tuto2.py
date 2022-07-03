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

driver.implicitly_wait(5)
sum1 = driver.find_element(By.ID, 'sum1').send_keys(Keys.NUMPAD1, Keys.NUMPAD5)

try:
    no_thanks_button = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
    no_thanks_button.click()
except:
    print("No element with this class name, skipping...")

sum2 = driver.find_element(By.ID, 'sum2').send_keys(Keys.NUMPAD2, Keys.NUMPAD5)
total = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]').click()

