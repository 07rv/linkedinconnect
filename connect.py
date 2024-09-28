from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from dotenv import load_dotenv

load_dotenv()
browser = webdriver.Chrome()


class Connect:
    user_name = os.getenv('USER_NAME')
    user_password = os.getenv('USER_PASSWORD')
    url = os.getenv('LINKEDIN_DOMAIN')
    time_sleep = int(os.getenv('SLEEP_TIME_HIGH'))

    def __init__(self):
        pass
    
    def login(self):
        try:
            url = f'{self.url}/login'
            browser.get(url=url)
            username = browser.find_element(By.ID, 'username')
            username.send_keys(self.user_name)
            password = browser.find_element(By.ID, 'password')
            password.send_keys(self.user_password)
            login_btn = browser.find_element(By.CLASS_NAME, 'btn__primary--large')
            login_btn.click()
        except Exception as e:
            print(e)


    def CompanyConnect(self,name):
        try:
            self.login()

            url = f'{self.url}/company/{name}/people'
            browser.get(url=url)
            time.sleep(self.time_sleep)

            users = browser.find_elements(By.CLASS_NAME, 'org-people-profile-card__profile-card-spacing')
            for user in users:
                userCardFooter = user.find_element(By.CLASS_NAME, 'ph3')
                button = userCardFooter.find_element(By.TAG_NAME, "button")

                buttonText = button.find_element(By.TAG_NAME, 'span').text

                if buttonText == 'Connect':
                    button.click()
                    time.sleep(5)
                    break

        except Exception as e:
            print(e)