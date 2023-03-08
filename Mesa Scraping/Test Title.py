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
import pandas

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
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    return driver

class mesaScraper:
    def __init__(self, url):
        self.base_url = url
        self.driver = get_webdriver()
        self.driver.get(self.base_url)

        '''--------------------Variables----------------------'''
        #Data
        self.pageLinkList = []
        self.productLinkList = []
        self.colorLinkList = []
        self.productTitleList = []
        self.productBrandList = []
        self.productModelList = []
        self.productPricePerSquareFeetList = []
        self.productPricePerCaseList = []
        self.storePickupStockList = []
        self.shipToHomeStockList = []
        self.scheduledDeliveryStockList = []

        #Selectors
        self.pageSelector = "a.hd-pagination__link"
        self.productSelectorList = ["#browse-search-pods-1 .desktop > div > a", "#browse-search-pods-2 .desktop > div > a.product-pod--ie-fix"]
        self.colorLinkSelector = "img.border-radius--medium"
        self.productTitleSelector = "h1"
        self.productBrandSelector = ".price-detailed__right-price-wrapper .price-detailed__unit-price span"
        self.productModelSelector = "h2:nth-of-type(2)"
        self.productPricePerSquareFeetSelector = ".price-detailed__left-price-wrapper .price-detailed__unit-price span"
        self.productPricePerCaseSelector = ".price-detailed__right-price-wrapper .price-detailed__unit-price span"
        # self.productShipmentTypeSelector = ".fulfillment__head div.u__bold"
        self.productShipmentTypeSelector = "a.card-enabled"
        self.productStockSelector = "span.u__text--success.u__bold"

        self.sequenceCaller()

    def sequenceCaller(self):
        self.getColorLinks()
        print(self.productTitleList)

    def getColorLinks(self):
        try:
            myElem6 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.productShipmentTypeSelector)))
            shipmentElements = self.driver.find_elements(By.CSS_SELECTOR, self.productShipmentTypeSelector)
            for element in shipmentElements:
                title = element.text
                sleep(5)
                element.click()
                sleep(5)
                if 'Store Pickup' in title:
                    try:
                        myElem7 = WebDriverWait(self.driver, 30).until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, self.productStockSelector)))
                        stockElements = self.driver.find_element(By.CSS_SELECTOR,
                                                                 self.productStockSelector)

                        stockStorePickup = stockElements.text
                        self.storePickupStockList.append(stockStorePickup)
                    except:
                        self.storePickupStockList.append('Null')
                else:
                    self.storePickupStockList.append('Null')

                if 'Ship to Home' in title:
                    try:
                        myElem8 = WebDriverWait(self.driver, 30).until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, self.productStockSelector)))
                        stockElements = self.driver.find_element(By.CSS_SELECTOR,
                                                                 self.productStockSelector)

                        stockShipToHome = stockElements.text
                        self.shipToHomeStockList.append(stockShipToHome)
                    except:
                        self.shipToHomeStockList.append('Null')
                else:
                    self.shipToHomeStockList.append('Null')

                if 'Scheduled Delivery' in title:
                    try:
                        myElem9 = WebDriverWait(self.driver, 30).until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, self.productStockSelector)))
                        stockElements = self.driver.find_element(By.CSS_SELECTOR,
                                                                 self.productStockSelector)

                        stockScheduleDelivery = stockElements.text
                        self.scheduledDeliveryStockList.append(stockScheduleDelivery)
                    except:
                        self.scheduledDeliveryStockList.append('Null')
                else:
                    self.scheduledDeliveryStockList.append('Null')

        except Exception as e:
            self.storePickupStockList.append('Null')
            self.shipToHomeStockList.append('Null')
            self.scheduledDeliveryStockList.append('Null')


        df = pandas.DataFrame(data={"Store Pickup": self.storePickupStockList, "Ship to Home": self.shipToHomeStockList, "Scheduled Delivery": self.scheduledDeliveryStockList})
        df.to_csv("./file.csv", sep=',', index=False)

if __name__=="__main__":
    URL = "https://www.homedepot.com/p/Lifeproof-Sterling-Oak-8-7-in-W-x-47-6-in-L-Click-Lock-Luxury-Vinyl-Plank-Flooring-20-06-sq-ft-case-I966106L/300699284"

    mesaScraper(url=URL)