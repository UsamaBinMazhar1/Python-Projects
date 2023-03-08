from time import sleep
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import pandas as pd
from bs4 import BeautifulSoup
import math

def get_webdriver(user_data_dir=None, headless=False):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.headless = headless
    if user_data_dir:
        chrome_options.add_argument('--user-data-dir=' + str(user_data_dir))
    driver = Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    return driver

class YoutubeBot:
    def __init__(self, email, password):
        self.Email = email
        self.Password = password
        self.url = "https://www.youtube.com/"
        self.driver = get_webdriver()
        self.driver.get(self.url)
        self.sequance_caller()

    def sequance_caller(self):
        sleep(2)
        self.driver.find_element_by_css_selector("tp-yt-paper-button.size-small").click()
        sleep(2)
        self.enterEmail()
        sleep(2)
        self.enterPassword()
        sleep(2)

    def enterEmail(self):
        css_selector = "input#identifierId"
        try:
            elements = self.driver.find_elements(By.CSS_SELECTOR, css_selector)
            elements[0].send_keys(self.Email)
            print(f"Info Email entered : {self.Email}")
            elements[0].send_keys(Keys.ENTER)
        except Exception as error:
            print(f"Error in Entering Email ==>{error}")

    def enterPassword(self):
        css_selector = ".ze9ebf input"
        try:
            elements = self.driver.find_elements(By.CSS_SELECTOR, css_selector)
            elements[0].send_keys(self.Password)
            print(f"Info Password entered : {self.Password}")
            elements[0].send_keys(Keys.ENTER)
        except Exception as error:
            print(f"Error in Entering Password ==>{error}")

if __name__ == '__main__':
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    bot = YoutubeBot(email=email, password=password)
