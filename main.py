from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "Email"
ACCOUNT_PASSWORD = "Password"
chrome_driver_path = "Chrome driver path"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_C=361424&f_WT=1%2C3%2C2&geoId=101620260&keywords=frontend%20developer&location=Israel")

signin_button = driver.find_element_by_link_text("Sign in")
signin_button.click()
time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(10)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
for listing in all_listings:
    listing.click()
    time.sleep(2)
    try:
        save_button = driver.find_element_by_css_selector(".jobs-save-button")
        save_button.click()
        time.sleep(5)
    except NoSuchElementException:
        continue

time.sleep(5)
driver.close()