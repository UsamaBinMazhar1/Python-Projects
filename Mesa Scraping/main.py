from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.options import Options

def get_webdriver(user_data_dir=None, headless=False):
    chrome_options = Options()
    # options = {
    #     "proxy": {
    #         "http": "http://P0P6J5BSTCSXSVK6XL51YKPHD6B8WDDHVMGFVBLGSS98LKX8HR0H1TI8GO9SY2YAEQ6GMCQ314HG2H35:render_js=False&premium_proxy=True@proxy.scrapingbee.com:8886",
    #         "verify_ssl": False,
    #     },
    # }
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.headless = headless
    if user_data_dir:
        chrome_options.add_argument('--user-data-dir=' + str(user_data_dir))
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    return driver



class mesaScraper:
    def __init__(self, url):
        self.base_url = url
        self.url_list=[]
        self.driver = get_webdriver()
        self.driver.get(self.base_url)
        #input('press Enter')
        # self.getLinks("#browse-search-pods-1 .desktop > div > a")
        # sleep(10)
        # self.getLinks("#browse-search-pods-2 .desktop > div > a.product-pod--ie-fix")
        self.getLinks("a.hd-pagination__link")

    def getLinks(self,selector):
        a = 0
        product_selector = selector
        try:
            myElem = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, product_selector)))
            print("element found")
            elements = self.driver.find_elements(By.CSS_SELECTOR, product_selector)
            # elements.click()
            # print('-------------------------------Clicked----------------------------------')
            for i, element in enumerate(elements):
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                links = element.get_attribute("href")
                print(f"{i}/{len(elements)}/",links)
                self.url_list.append(links)

        except Exception as e:
            print(f"element not found")


if __name__=="__main__":
    URL = "http://www.homedepot.com/b/Same-Day-Delivery/Click-Lock/N-5yc1vZ1z175cqZ1z1ajwk/Ntk-elasticplus/Ntt-lvp?NCNI-5&sortby=bestmatch&sortorder=none"

    mesaScraper(url=URL)




