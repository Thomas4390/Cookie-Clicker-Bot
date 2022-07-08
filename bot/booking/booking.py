from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Booking(webdriver.Chrome):

    def __init__(self):

        service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
        driver.maximize_window()

    def land_first_page(self):
        self.get
