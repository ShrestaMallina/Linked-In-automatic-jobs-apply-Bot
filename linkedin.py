from logging import exception
from os import abort

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4226175885&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
driver.maximize_window()
#linkedin signin button


#automatic applying jobs

def abort_application():
    wrong = driver.find_element(By.CSS_SELECTOR,value="button[aria-label='Dismiss']")
    wrong.click()
    discard = driver.find_element(By.CSS_SELECTOR,value="[data-control-name='discard_application_confirm_btn']")
    discard.click()

while True:
    sign_in = driver.find_element(By.XPATH,value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
    sign_in.click()

    #signin form

    email = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
    password = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
    sign_up = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
    email.send_keys("your gamil.com")
    password.send_keys("Linkedin password")
    sign_up.click()

    driver.implicitly_wait(15)
    job_clicks = driver.find_elements(By.CLASS_NAME,value='ember-view a')

    for job in job_clicks:
        job.click()
        time.sleep(2)
        try:
           easy_apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
           easy_apply.click()
           next_button = driver.find_element(By.CSS_SELECTOR, value="button[aria-label = 'continue to next step']")
           next_button.click()
           time.sleep(2)
           review_button = driver.find_element(By.CSS_SELECTOR, value="button[aria-label='Review your application']")
           review_button.click()
           time.sleep(2)
           submit_application = driver.find_element(By.CSS_SELECTOR, value="button[aria-label='Submit application']")
           if submit_application.get_attribute("data-control-name")=="continue-unify":
              abort_application()
              continue
           else:
              submit_application.click()
           time.sleep(2)
           # Click Close Button
        except exception:
              close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
              close_button.click()







