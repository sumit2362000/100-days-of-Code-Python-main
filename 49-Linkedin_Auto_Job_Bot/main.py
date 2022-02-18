
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

SLEEP_TIME = 2

ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""
PHONE = ""

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

'''Python Developer in certain locations for internships'''
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1&f_PP=102277331%2C102448103%2C104116203%2C106233382&keywords=python&sortBy=R"

driver.get(URL)
time.sleep(SLEEP_TIME)

'''Sign in'''
sign_in_button = driver.find_element_by_link_text("Sign in") 
sign_in_button.click()
time.sleep(SLEEP_TIME)
email_field  = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(SLEEP_TIME)
not_now = driver.find_element_by_class_name("btn__secondary--large-muted")
not_now.click()
time.sleep(SLEEP_TIME)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    #Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)
        
        #If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
    
        #Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    #If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()