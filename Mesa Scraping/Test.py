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
        self.productColorList = []
        self.productWeightList = []
        self.piecesPerCaseList = []

        #Selectors
        self.pageSelector = "a.hd-pagination__link"
        self.productSelectorList = ["#browse-search-pods-1 .desktop > div > a", "#browse-search-pods-2 .desktop > div > a.product-pod--ie-fix"]
        self.colorLinkSelector = "img.border-radius--medium"
        self.productTitleSelector = "h1"
        self.productBrandSelector = "h2.product-details__brand--link"
        self.productModelSelector = "h2:nth-of-type(2)"
        self.productPricePerSquareFeetSelector = ".price-detailed__left-price-wrapper .price-detailed__unit-price span"
        self.productPricePerCaseSelector = ".price-detailed__right-price-wrapper .price-detailed__unit-price span"
        self.productColorSelector = ""
        self.productWeightSelector = ""
        self.piecesPerCaseSelector = ""
        self.specificationSelector = ""

        self.sequenceCaller()

    def sequenceCaller(self):
        self.getColorLinks()

    def getData(self):
        try:
            myElem = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.colorLinkSelector)))
            elements = self.driver.find_elements(By.CSS_SELECTOR, self.colorLinkSelector)

            for i, element in enumerate(elements):
                try:
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    sleep(5)
                    element.click()
                    sleep(5)
                    myElem1 = WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, self.productTitleSelector)))
                    titleElement = self.driver.find_element(By.TAG_NAME, self.productTitleSelector)
                    title = titleElement.text
                    self.productTitleList.append(title)
                    print(f'{i}--/{title}')

                    sleep(5)
                    myElem2 = WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, self.productBrandSelector)))
                    brandElement = self.driver.find_element(By.CSS_SELECTOR, self.productBrandSelector)
                    brand = brandElement.text
                    self.productBrandList.append(brand)
                    print(f'{i}--/{brand}')

                    sleep(5)
                    myElem3 = WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, self.productModelSelector)))
                    modelElement = self.driver.find_element(By.CSS_SELECTOR, self.productModelSelector)
                    model = modelElement.text
                    self.productModelList.append(model)
                    print(f'{i}--/{model}')

                    sleep(5)
                    myElem4 = WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, self.productPricePerSquareFeetSelector)))
                    priceFtElement = self.driver.find_element(By.CSS_SELECTOR, self.productPricePerSquareFeetSelector)
                    priceFt = priceFtElement.text
                    self.productPricePerSquareFeetList.append(priceFt)
                    print(f'{i}--/{priceFt}')

                    sleep(5)
                    myElem5 = WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, self.productPricePerCaseSelector)))
                    priceCaseElement = self.driver.find_element(By.CSS_SELECTOR, self.productPricePerCaseSelector)
                    priceCase = priceCaseElement.text
                    self.productPricePerCaseList.append(priceCase)
                    print(f'{i}--/{priceCase}')



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



            #
            # # self.productTitleList = list(dict.fromkeys(self.productLinkList))
            # sleep(10)
            #
            # print('Product Titles', len(self.productTitleList))
            # print(self.productTitleList)

        except Exception as e:
            print('Titles Not Found')


if __name__=="__main__":
    URL = "https://www.homedepot.com/p/Lifeproof-Sterling-Oak-8-7-in-W-x-47-6-in-L-Click-Lock-Luxury-Vinyl-Plank-Flooring-20-06-sq-ft-case-I966106L/300699284"

    mesaScraper(url=URL)