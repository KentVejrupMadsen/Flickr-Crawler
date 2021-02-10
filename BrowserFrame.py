from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


import time

class BrowserFrame:
    __browser = None
    __options = None

    def __init__(self):
        self.setup_chrome()
        pass

    def setup_chrome(self):
        self.__options = webdriver.ChromeOptions()
        self.__options.add_argument("user-data-dir=D:\\Workspace\\flickr-crawler\\user-data")
        self.__browser = webdriver.Chrome( options=self.__options)

    def load(self, url):
        self.__browser.get(url)

    def get_image(self):
        try:
            download = self.__browser.find_element(By.CLASS_NAME, 'download')
            download.click()

            time.sleep(1)

            el = self.__browser.find_element(By.CLASS_NAME, 'Original')
            el.click()

        except Exception as e:
            print('Found Error: ')
            print( e.__class__ )

    def next(self):
        next_el = self.__browser.find_element(By.CLASS_NAME, 'navigate-next')
        link = next_el.get_attribute('href')
        self.load(link)

    def is_done(self):
        if(self.__browser is not None):
            self.__browser.close()