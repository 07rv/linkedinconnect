from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()
browser = webdriver.Chrome()


class Connect:
    user_name = os.getenv('USER_NAME')
    password = os.getenv('USER_PASSWORD')
    url = os.getenv('LINKEDIN_DOMAIN')
    
    def login(self):
        try:
            browser.get(f'${self.url}/login')
            # username = browser.find_element(By.ID, 'session_key')
            # username.send_keys(self.user_email)
            # password = browser.find_element(By.ID, 'session_password')
            # password.send_keys(self.user_password)
            # login_btn = browser.find_element(By.CLASS_NAME, 'sign-in-form__submit-btn--full-width')
            # login_btn.click()
        except Exception as e:
            print(e)