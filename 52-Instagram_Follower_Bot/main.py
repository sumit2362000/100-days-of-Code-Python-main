
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
TARGET_ACCOUNT = "chefsteps"
USERNAME = "ambotdonotfollow"
PASSWORD = "seleniumpractice"

class InstaFollower():
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
    
    def login(self):
        '''Login to Instagram'''
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        time.sleep(1.5)
        username_field = self.driver.find_element_by_name('username')
        username_field.send_keys(USERNAME)
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(PASSWORD)
        time.sleep(1)
        password_field.send_keys(Keys.ENTER)
        time.sleep(2)
    
    def find_followers(self):
        '''Go to account followers'''
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}")
        time.sleep(1.5)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(1.5)
        '''Followers pop up'''
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()