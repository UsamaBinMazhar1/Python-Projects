from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome, ActionChains


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


driver = get_webdriver()
df = pd.read_excel("IMP_Bot_file.xlsx")


class Soial_Media_Bots:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.sequance()

    def sequance(self):
        Youtube_bot(email=self.email, password=self.password, keyword=str(df.iloc[0]['Keywords']),
                    range=int(df.iloc[0]['Number of interactions per day']), dalay_time=int(df.iloc[0]['Time frame between each interaction']))
        try:
            FacebookBot(email=str(df.iloc[1]['Emial']), password=str(df.iloc[1]['Password']),
                        keyword=str(df.iloc[1]['Keywords']), range_=int(df.iloc[1]['Number of interactions per day']),
                        dalay_time=int(df.iloc[1]['Time frame between each interaction']))
        except:
            pass
        try:
            TwitterBot(email=str(df.iloc[2]['Emial']), password=str(df.iloc[2]['Password']),
                       keyword=str(df.iloc[2]['Keywords']),
                       range_=int(df.iloc[2]['Number of interactions per day']), dalay_time=int(df.iloc[2]['Time frame between each interaction']))
        except:
            pass
        try:
            RedditBot(email=str(df.iloc[3]['Emial']), password=str(df.iloc[3]['Password']),
                      keyword=str(df.iloc[3]['Keywords']), range_=int(df.iloc[3]['Number of interactions per day']),
                      dalay_time=int(df.iloc[3]['Time frame between each interaction']))

        except:
            pass
        try:
            TumblerBot(email=str(df.iloc[4]['Emial']), password=str(df.iloc[4]['Password']),
                       keyword=str(df.iloc[4]['Keywords']), range_=int(df.iloc[4]['Range']),
                       dalay_time=int(df.iloc[4]['Time frame between each interaction']))
        except:
            pass
        try:
            Pinterest_Bot(email=str(df.iloc[5]['Emial']), password=str(df.iloc[5]['Password']),
                          keyword=str(df.iloc[5]['Keywords']), range_=int(df.iloc[5]['Number of interactions per day']),
                          dalay_time=int(df.iloc[5]['Time frame between each interaction']))

        except:
            pass


class Youtube_bot:
    def __init__(self, email, password, keyword, range, dalay_time):
        self.url = "https://www.youtube.com/"
        self.keyword = keyword
        self.dalay_time = dalay_time
        self.range = range
        self.video_link_list = []
        self.email = email
        self.password = password
        driver.get(self.url)

        self.selector_dic = {'signIn_btn': '#buttons > ytd-button-renderer > a',
                             'email_textbox': '#identifierId',
                             'password_textbox': '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input',
                             'search_textbox': '#search',
                             'link_btn': 'ytd-toggle-button-renderer.ytd-menu-renderer:nth-of-type(1) a',
                             'filter': 'tp-yt-paper-button.ytd-toggle-button-renderer',
                             'upload_data': '.style-scope:nth-child(1) > .style-scope:nth-child(4) > #endpoint > #label > .style-scope:nth-child(1)',
                             'view_count': '.ytd-search-sub-menu-renderer #text',
                             'videos': '#video-title'}
        self.sequance_caller()

    def sequance_caller(self):
        self.click_on_btn(selector=self.selector_dic['signIn_btn'], name='signIn_btn')
        sleep(2)
        self.enter_data_in_textbox(selector=self.selector_dic['email_textbox'], U_input=self.email,
                                   name="email_textbox", click=True)
        sleep(3)
        self.enter_data_in_textbox(selector=self.selector_dic['password_textbox'], U_input=self.password,
                                   name="password_textbox", click=True)
        sleep(5)
        driver.get(
            f"https://www.youtube.com/results?search_query={str(self.keyword).replace(' ', '+')}&sp=CAMSBAgCEAE%253D")
        # self.enter_query()
        # sleep(2)
        # self.click_on_btn(selector=self.selector_dic['filter'], name='filter')
        # sleep(1)
        # self.click_on_btn(selector=self.selector_dic['upload_data'], name='upload_data')
        # sleep(1)
        # self.click_on_btn(selector=self.selector_dic['view_count'], name='view_count')
        sleep(3)
        for i in range(0, self.range):
            if len(self.video_link_list) < self.range:
                self.get_all_link_of_video(self.selector_dic['videos'], counter=i)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            else:
                break

        for i in range(0, self.range):
            self.like_video(link=self.video_link_list[i], counter=i)
            sleep(self.dalay_time)

    def enter_query(self):
        name_selector = "search_query"
        try:
            myElem = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.NAME, name_selector)))
            element = driver.find_element(By.NAME, name_selector)
            element.click()
            sleep(1)
            element.send_keys(self.keyword)
            sleep(2)
            element.send_keys(Keys.ENTER)
            print(f"Info {self.keyword} enter in search box")
            return True

        except Exception as error:
            print(f"Error {self.keyword} not enter  ==> {error}")
            return False

    def click_on_btn(self, selector, name):
        try:
            myElem = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
            element = driver.find_element(By.CSS_SELECTOR, selector)
            driver.execute_script("arguments[0].click();", element)
            print(f"Info Click on {name} Btn")
            return True

        except Exception as error:
            print(f"Error click {name} btn ==> {error}")
            return False

    def enter_data_in_textbox(self, selector, U_input, name, click):
        try:
            myElem = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

            element = driver.find_element(By.CSS_SELECTOR, selector)
            element.send_keys(U_input)
            if click:
                element.send_keys(Keys.ENTER)
            print(f"Info {name} Data inserted")
        except Exception as error:
            print(
                f"Error unable to enter value of {name} ==> {error}")

    def get_all_link_of_video(self, selector, counter):

        try:
            myElem = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            for index, element in enumerate(elements):
                driver.execute_script("arguments[0].scrollIntoView();", element)
                try:
                    video_link = str(element.get_attribute('href'))
                    if 'watch?' in video_link:
                        self.video_link_list.append(f"{video_link}")
                        print(f"Info Link {index * counter} ==> {video_link}")
                except:
                    continue

        except Exception as error:
            print(f"Error getting  link ==> {error}")

    def like_video(self, link, counter):
        driver.get(link)
        if self.click_on_btn(selector=self.selector_dic['link_btn'], name="like_btn"):
            print(f"Info {counter} | like btn clicked ==> {link}")
        else:
            print(f"Error {counter} | in like video ==> {link}")


class FacebookBot:
    def __init__(self, email, password, keyword, range_, dalay_time):
        self.email = email
        self.keyword = keyword
        self.password = password
        self.range = range_
        self.dalay_time = dalay_time
        self.counter = 0
        self.url = "https://www.facebook.com/"
        driver.get(self.url)
        self.sequance_caller()

    def sequance_caller(self):
        self.login()
        driver.get(
            f"https://www.facebook.com/search/posts?q={str(self.keyword).replace(' ', '%20')}&filters=eyJyZWNlbnRfcG9zdHM6MCI6IntcIm5hbWVcIjpcInJlY2VudF9wb3N0c1wiLFwiYXJnc1wiOlwiXCJ9In0%3D")

        for i in range(0, self.range):
            if self.counter < self.range:
                self.like_post()

    def login(self):
        css_selector = "input#email, input._9npi"
        try:
            myElem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
            elements[0].send_keys(self.email)
            print(f"Info Email entered : {self.email}")
            elements[1].send_keys(self.password)
            print(f"Info Password entered : ")
            sleep(1)
            elements[1].send_keys(Keys.ENTER)
            sleep(3)
            print(f"Info Login Successfully")

        except Exception as error:
            print(f"Error in login ==>{error}")

    def like_post(self):
        css_selector = "[aria-label='Like'] div.g5gj957u"
        try:
            myElem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
            for index, element in enumerate(elements):
                if self.counter < self.range:
                    driver.execute_script("arguments[0].scrollIntoView();", element)
                    driver.execute_script("arguments[0].click();", element)
                    self.counter = self.counter + 1
                    print(f"Info {self.counter} Clicked!")
                    sleep(self.dalay_time)

        except Exception as error:
            print(f"Error in like Post ==>{error}")


class TwitterBot:
    def __init__(self, email, password, keyword, range_, dalay_time):
        self.email = email
        self.keyword = keyword
        self.range = range_
        self.counter = 0
        self.dalay_time = dalay_time
        self.password = password
        self.mysearch = "marketing"
        self.url = "https://twitter.com/i/flow/login"
        driver.get(self.url)
        self.sequance_caller()

    def sequance_caller(self):
        self.enter_email()
        self.enter_password()
        driver.get(f"https://twitter.com/search?q={str(self.keyword).replace(' ', '%20')}&src=typed_query&f=live")
        for i in range(0, self.range):
            if self.counter < self.range:
                self.like()

    def enter_email(self):
        css_selector = "#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input"
        try:
            myElem = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
            elements[0].send_keys(self.email)
            print(f"Info Email entered : {self.email}")
            sleep(2)
            elements[0].send_keys(Keys.ENTER)
            sleep(1)
            print(f"Info Email Entered Successfully")

        except Exception as error:
            print(f"Error in enter_email ==>{error}")

    def enter_password(self):
        css_selector = "#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div:nth-child(3) > div > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input"
        try:
            myElem = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
            elements[0].send_keys(self.password)
            print(f"Info Password entered :")
            sleep(2)
            elements[0].send_keys(Keys.ENTER)
            sleep(1)
            print(f"Info Password Entered Successfully")

        except Exception as error:
            print(f"Error in enter_password ==>{error}")

    def like(self):
        actions = ActionChains(driver)

        css_selector = "[aria-label='0 Likes. Like'] svg"
        try:
            myElem = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
            for index, element in enumerate(elements):
                if self.counter < self.range:
                    try:
                        actions.move_to_element(elements[index]).move_to_element(elements[index + 1]).click().perform()
                        self.counter = self.counter + 1
                        print(f"Info {self.counter} Clicked!")
                        sleep(self.dalay_time)
                    except:
                        pass


        except Exception as error:
            print(f"Error in like ==>{error}")




class RedditBot:
    def __init__(self, email, password, keyword, range_, dalay_time):
        self.url = "https://www.reddit.com/login/"

        self.keyword = keyword
        self.range = range_
        self.dalay_time=dalay_time
        self.email = email
        self.password = password
        self.link_list = []
        self.index = 0
        self.counter = 0
        driver.get(self.url)

        self.selector_dic = {'email': "input#loginUsername",
                             'password': "input#loginPassword"}

        self.sequance_caller()

    def sequance_caller(self):
        self.enter_data_in_textbox(selector=self.selector_dic['email'], U_input=self.email,
                                   name="email", click=False)
        self.enter_data_in_textbox(selector=self.selector_dic['password'], U_input=self.password,
                                   name="password", click=True)
        print(f"Info Login successfully")
        sleep(5)

        driver.get(
            f"https://www.reddit.com/search/?q={str(self.keyword).replace(' ', '%20')}&sort=new")

        for i in range(0, self.range):
            if self.counter < self.range:
                self.get_all_link()
        for i in range(0, self.range):
            driver.get(self.link_list[i])
            self.click_on_btn(selector=".icon-upvote", name="up vote btn")
            sleep(self.dalay_time)

    def click_on_btn(self, selector, name):
        try:
            myElem = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
            element = driver.find_element(By.CSS_SELECTOR, selector)
            element.click()
            # driver.execute_script("arguments[0].click();", element)
            print(f"Info Click on {name} Btn")
            return True

        except Exception as error:
            print(f"Error click {name} btn ==> {error}")
            return False

    def get_all_link(self):
        selector = "a.SQnoC3ObvgnGjWt90zD9Z"
        try:
            myElem = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            for index, element in enumerate(elements):
                if self.counter < self.range:
                    driver.execute_script("arguments[0].scrollIntoView();", element)
                    link = element.get_attribute('href')
                    print(f"Info {self.counter} | {link}")
                    self.link_list.append(link)
                    self.counter = self.counter + 1

        except Exception as error:
            print(f"Error in Clicking post ==> {error}")
            return False

    def enter_data_in_textbox(self, selector, U_input, name, click):
        try:
            myElem = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

            element = driver.find_element(By.CSS_SELECTOR, selector)
            element.send_keys(U_input)
            if click:
                element.send_keys(Keys.ENTER)
            print(f"Info {name} Data inserted")
        except Exception as error:
            print(
                f"Error unable to enter value of {name} ==> {error}")


class TumblerBot:
    def __init__(self, email, password, keyword, range_, dalay_time):
        self.tumbler_url = "https://www.tumblr.com/login"

        self.keyword = keyword
        self.range = range_
        self.email = email
        self.password = password
        self.dalay_time = dalay_time
        driver.get(self.tumbler_url)

        self.selector_dic = {'email': "input.o4KIk[type='text']",
                             'password': "input[type='password']",
                             'post': 'article',
                             'like_btn': "[data-id='667103841634893824'] .xG22D path"}

        self.sequance_caller()

    def sequance_caller(self):

        self.enter_data_in_textbox(selector=self.selector_dic['email'], U_input=self.email,
                                   name="email", click=False)
        self.enter_data_in_textbox(selector=self.selector_dic['password'], U_input=self.password,
                                   name="password", click=True)
        print(f"Info Login successfully")
        sleep(5)
        driver.get(f"https://www.tumblr.com/search/{str(self.keyword).replace(' ', '+')}/recent")
        self.click_article()

    def click_article(self):
        selector = "article"
        try:
            myElem = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            for element in range(0, self.range):
                try:
                    myElem = WebDriverWait(driver, 5).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, "xBRdB")))
                    elements[element].find_element(By.CLASS_NAME, "xBRdB").click()
                    print(f"Info {element} Clicked!")
                    sleep(self.dalay_time)
                except Exception as error:
                    print(f"Error click {element} article ==> {error}")

        except Exception as error:
            print(f"Error in finding article btn ==> {error}")
            return False

    def enter_data_in_textbox(self, selector, U_input, name, click):
        try:
            myElem = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

            element = driver.find_element(By.CSS_SELECTOR, selector)
            element.send_keys(U_input)
            if click:
                element.send_keys(Keys.ENTER)
            print(f"Info {name} Data inserted")
        except Exception as error:
            print(
                f"Error unable to enter value of {name} ==> {error}")


class Pinterest_Bot:
    def __init__(self, email, password, keyword, range_, dalay_time):
        self.email = email
        self.password = password
        self.counter = 0
        self.range = range_
        self.keyword = keyword
        self.dalay_time = dalay_time
        self.link_list = []
        self.url = "https://www.pinterest.com/login/"
        driver.get(self.url)
        self.sequance_caller()

    def sequance_caller(self):
        self.login()
        driver.get((f"https://www.pinterest.com/search/pins/?q={str(self.keyword).replace(' ', '%20')}"))
        for i in range(0, self.range):
            self.select_image(i)
            self.select_video(i)
            sleep(self.dalay_time)

    def select_image(self, i):
        selector = f'//*[@id="__PWS_ROOT__"]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[{i + 2}]/div/div/div/div/div[1]/div[1]/a/div/div[1]/div/div/div/div'
        try:
            myElem = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, selector)))
            elements = driver.find_element(By.XPATH, selector)
            driver.execute_script("arguments[0].scrollIntoView();", elements)
            elements.click()
            if self.like_post():
                pass
            else:
                driver.back()
        except Exception as error:
            print(f"Error in Selecting Image  ==>{error}")

    def select_video(self, i):
        selector = f'//*[@id="__PWS_ROOT__"]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[{i + 2}]/div/div/div/div/div[1]/div[1]/a/div/div[1]/div/div/div/div/video'
        try:
            myElem = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, selector)))
            elements = driver.find_element(By.XPATH, selector)
            driver.execute_script("arguments[0].scrollIntoView();", elements)
            elements.click()
            if self.like_post():
                pass
            else:
                driver.back()

        except Exception as error:
            print(f"Error in Selecting Video  ==>{error}")

    def like_post(self):
        css_selector = ".gjz.hs0 .XiG .INd > div.Jea"
        try:
            myElem = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            element = driver.find_element(By.CSS_SELECTOR, css_selector)
            driver.execute_script("arguments[0].click();", element)
            print(f"Info post like")
            driver.back()
            return True
        except Exception as error:
            print(f"Error in finding like Post ==>{error}")
            return False

    def login(self):
        css_selector = "input"
        try:
            myElem = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            elements = driver.find_elements(By.CSS_SELECTOR, css_selector)

            elements[0].send_keys(self.email)
            print(f"Info Email entered : {self.email}")

            elements[1].send_keys(self.password)
            print(f"Info Password entered : ")

            sleep(1)
            elements[1].send_keys(Keys.ENTER)
            sleep(3)
            print(f"Info Login Successfully")

        except Exception as error:
            print(f"Error in login ==>{error}")


if __name__ == "__main__":
    email = df.iloc[0]['Emial']
    password = df.iloc[0]['Password']
    Soial_Media_Bots(email=email, password=password)
