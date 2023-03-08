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
        self.productBrandSelector = "h2.product-details__brand--link"
        self.productModelSelector = "h2:nth-of-type(2)"
        self.productPricePerSquareFeetSelector = ".price-detailed__left-price-wrapper .price-detailed__unit-price span"
        self.productPricePerCaseSelector = ".price-detailed__right-price-wrapper .price-detailed__unit-price span"
        self.productShipmentTypeSelector = "a.card-enabled"
        self.productStockSelector = "span.u__text--success.u__bold"

        self.sequenceCaller()

    def sequenceCaller(self):
        self.getPageLinks()
        sleep(10)
        self.getProductLinks()
        sleep(10)
        self.getData()
        sleep(10)
        df = pandas.DataFrame(data={"Title": self.productTitleList, "Brand": self.productBrandList,
                                    "Model": self.productModelList, "Price/Sq ft.": self.productPricePerSquareFeetList,
                                    "Price/Case": self.productPricePerCaseList, "Store Pick Stock": self.storePickupStockList,
                                    "Ship to Home Stock": self.shipToHomeStockList, "Schedule Delivery Stock": self.scheduledDeliveryStockList})
        df.to_csv("./allDataFile.csv", sep=',', index=False)

    def getPageLinks(self):
        try:
            myElem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.pageSelector)))
            elements = self.driver.find_elements(By.CSS_SELECTOR, self.pageSelector)

            for i, element in enumerate(elements):
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                links = element.get_attribute("href")

                self.pageLinkList.append(links)

            self.pageLinkList = list(dict.fromkeys(self.pageLinkList))
            print('Page Links', self.pageLinkList)

        except Exception as e:
            print(f"element not found")

    def getProductLinks(self):
        try:
            for pageLink in self.pageLinkList:
                self.driver.get(pageLink)
                for productSelector in self.productSelectorList:
                    try:
                        myElem = WebDriverWait(self.driver, 30).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, productSelector)))
                        elements = self.driver.find_elements(By.CSS_SELECTOR, productSelector)

                        for i, element in enumerate(elements):
                            self.driver.execute_script("arguments[0].scrollIntoView();", element)
                            links = element.get_attribute("href")
                            print(f'{i}--/{links}')
                            self.productLinkList.append(links)

                        self.productLinkList = list(dict.fromkeys(self.productLinkList))
                    except:
                        continue

                sleep(10)
            print('Product Links', len(self.productLinkList))
            print(self.productLinkList)

        except Exception as e:
            print('links not found')

    def getData(self):
        try:
            for productLink in self.productLinkList:
                self.driver.get(productLink)
                myElem = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, self.colorLinkSelector)))
                elements = self.driver.find_elements(By.CSS_SELECTOR, self.colorLinkSelector)

                for i, element in enumerate(elements):
                    try:
                        self.driver.execute_script("arguments[0].scrollIntoView();", element)
                        sleep(5)
                        element.click()

                        try:
                            sleep(5)
                            myElem1 = WebDriverWait(self.driver, 30).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, self.productTitleSelector)))
                            titleElement = self.driver.find_element(By.TAG_NAME, self.productTitleSelector)
                            title = titleElement.text
                            self.productTitleList.append(title)
                            print(f'{i}--/{title}')
                        except:
                            self.productTitleList.append('Null')

                        try:
                            sleep(5)
                            myElem2 = WebDriverWait(self.driver, 30).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, self.productBrandSelector)))
                            brandElement = self.driver.find_element(By.CSS_SELECTOR, self.productBrandSelector)
                            brand = brandElement.text
                            self.productBrandList.append(brand)
                            print(f'{i}--/{brand}')
                        except:
                            self.productBrandList.append('Null')

                        try:
                            sleep(5)
                            myElem3 = WebDriverWait(self.driver, 30).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, self.productModelSelector)))
                            modelElement = self.driver.find_element(By.CSS_SELECTOR, self.productModelSelector)
                            model = modelElement.text
                            self.productModelList.append(model)
                            print(f'{i}--/{model}')
                        except:
                            self.productModelList.append('Null')

                        try:
                            sleep(5)
                            myElem4 = WebDriverWait(self.driver, 30).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, self.productPricePerSquareFeetSelector)))
                            priceFtElement = self.driver.find_element(By.CSS_SELECTOR,
                                                                      self.productPricePerSquareFeetSelector)
                            priceFt = priceFtElement.text
                            self.productPricePerSquareFeetList.append(priceFt)
                            print(f'{i}--/{priceFt}')
                        except:
                            self.productPricePerSquareFeetList.append('Null')

                        try:
                            sleep(5)
                            myElem5 = WebDriverWait(self.driver, 30).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, self.productPricePerCaseSelector)))
                            priceCaseElement = self.driver.find_element(By.CSS_SELECTOR, self.productPricePerCaseSelector)
                            priceCase = priceCaseElement.text
                            self.productPricePerCaseList.append(priceCase)
                            print(f'{i}--/{priceCase}')
                        except:
                            self.productPricePerCaseList.append('Null')

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
                                        print(f'Store Pickup--/{stockStorePickup}')
                                        self.storePickupStockList.append(stockStorePickup)
                                    except:
                                        print(f'Store Pickup--/Null')
                                        self.storePickupStockList.append('Null')
                                else:
                                    print(f'Store Pickup--/Null')
                                    self.storePickupStockList.append('Null')

                                if 'Ship to Home' in title:
                                    try:
                                        myElem8 = WebDriverWait(self.driver, 30).until(
                                            EC.presence_of_element_located(
                                                (By.CSS_SELECTOR, self.productStockSelector)))
                                        stockElements = self.driver.find_element(By.CSS_SELECTOR,
                                                                                 self.productStockSelector)

                                        stockShipToHome = stockElements.text
                                        print(f'Ship to Home--/{stockShipToHome}')
                                        self.shipToHomeStockList.append(stockShipToHome)
                                    except:
                                        print(f'Ship to Home--/Null')
                                        self.shipToHomeStockList.append('Null')
                                else:
                                    print(f'Ship to Home--/Null')
                                    self.shipToHomeStockList.append('Null')

                                if 'Scheduled Delivery' in title:
                                    try:
                                        myElem9 = WebDriverWait(self.driver, 30).until(
                                            EC.presence_of_element_located(
                                                (By.CSS_SELECTOR, self.productStockSelector)))
                                        stockElements = self.driver.find_element(By.CSS_SELECTOR,
                                                                                 self.productStockSelector)

                                        stockScheduleDelivery = stockElements.text
                                        print(f'Scheduled Delivery--/{stockScheduleDelivery}')
                                        self.scheduledDeliveryStockList.append(stockScheduleDelivery)
                                    except:
                                        print(f'Scheduled Delivery--/Null')
                                        self.scheduledDeliveryStockList.append('Null')
                                else:
                                    print(f'Scheduled Delivery--/Null')
                                    self.scheduledDeliveryStockList.append('Null')

                        except Exception as e:
                            self.storePickupStockList.append('Null')
                            self.shipToHomeStockList.append('Null')
                            self.scheduledDeliveryStockList.append('Null')
                            print('All Shipment Null')

                        try:
                            df = pandas.DataFrame(data={"Title": self.productTitleList, "Brand": self.productBrandList,
                                                        "Model": self.productModelList,
                                                        "Price/Sq ft.": self.productPricePerSquareFeetList,
                                                        "Price/Case": self.productPricePerCaseList,
                                                        "Store Pick Stock": self.storePickupStockList,
                                                        "Ship to Home Stock": self.shipToHomeStockList,
                                                        "Schedule Delivery Stock": self.scheduledDeliveryStockList})
                            df.to_csv("./file.csv", sep=',', index=False)
                        except:
                            continue

                    except:
                        print(f'{i} Passed')
                        continue

                print('Product Titles', len(self.productTitleList))
                print(self.productTitleList)

                print('Product Brand', len(self.productBrandList))
                print(self.productBrandList)

                print('Product Model', len(self.productModelList))
                print(self.productModelList)

                print('Product Price/Ft.', len(self.productPricePerSquareFeetList))
                print(self.productPricePerSquareFeetList)

                print('Product Price/case', len(self.productPricePerCaseList))
                print(self.productPricePerCaseList)
                sleep(5)

        except Exception as e:
            self.productLinkList = []
            self.getProductLinks()


if __name__=="__main__":
    URL = "http://www.homedepot.com/b/Same-Day-Delivery/Click-Lock/N-5yc1vZ1z175cqZ1z1ajwk/Ntk-elasticplus/Ntt-lvp?NCNI-5&sortby=bestmatch&sortorder=none"

    mesaScraper(url=URL)