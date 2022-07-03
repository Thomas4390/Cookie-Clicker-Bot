#!/usr/local/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def get_driver():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
    return driver

def driver_actions():
    
    download_button = driver.find_element(By.ID, 'downloadButton')
    download_button.click()

    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'progress-label'), 'Complete!')
    )

    simple_form = driver.find_element(By.LINK_TEXT, 'Input Forms')
    simple_form.click()
    driver.implicitly_wait(10)
    simple_form_demo = driver.find_element(By.LINK_TEXT, 'Simple Form Demo')
    simple_form_demo.click()

    sum1 = driver.find_element(By.ID, 'sum1').send_keys(Keys.NUMPAD1, Keys.NUMPAD5)

    try:
        no_thanks_button = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
        no_thanks_button.click()
    except:
        print("No element with this class name, skipping...")

    sum2 = driver.find_element(By.ID, 'sum2').send_keys(Keys.NUMPAD2, Keys.NUMPAD5)
    total = driver.find_element(
        By.CSS_SELECTOR, 'button[onclick="return total()"]').click()


    time.sleep(20)


if __name__ == '__main__':
    driver = get_driver()
    driver_actions()






