
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

TWITTER_LOGIN = "SeleniumPracti2"
TWITTER_PASS = "seleniumtest"
internet_provider = "INPUT INTERNET SERVICE PROVIDER"
PROMISED_DOWN = 150 #INPUT PROMISED DOWNLOAD SPEED
PROMISED_UP = 10 #INPUT PROMISED UPLOAD SPEED
CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0
    
    def get_internet_speed(self):
        '''SpeedTest'''
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        time.sleep(4)
        speed_test_go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        speed_test_go_button.click()
        '''Get Download and Upload Speed'''
        time.sleep(40)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
    
    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            '''Twitter Login''' 
            self.driver.get("https://twitter.com/login")
            self.driver.maximize_window()
            time.sleep(4)
            twitter_email_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            twitter_email_field.send_keys(TWITTER_LOGIN)
            twitter_password_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
            twitter_password_field.send_keys(TWITTER_PASS)
            time.sleep(2)
            twitter_password_field.send_keys(Keys.ENTER)
            time.sleep(5)
            '''Twitter Post'''
            tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')

            tweet = f"Hey {internet_provider}, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            tweet_compose.send_keys(tweet)
            time.sleep(3)
            tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
            tweet_button.click()
            time.sleep(2)
            self.driver.quit()   
        else:
            print("They delivered their promised speeds, no complaint necessary...")

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()