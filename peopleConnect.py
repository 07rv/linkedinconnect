from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
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
    
    def __login(self):
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

    def __PeopleConnect(self,name, page_limit = 3):
        try:
            url = f'{self.url}/search/results/people/?keywords=/{name}'
            browser.get(url=url)

            prev_height = -1 
            max_scrolls = 3
            scroll_count = 0
            while scroll_count < max_scrolls:
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                new_height = browser.execute_script("return document.body.scrollHeight")
                if new_height == prev_height:
                    break
                prev_height = new_height
                scroll_count += 1

            totalPages = browser.find_elements(By.CLASS_NAME, 'artdeco-pagination__indicator--number')
            if len(totalPages) > 0:
                totalPages = totalPages[-1]
                totalPages = int(totalPages.find_element(By.TAG_NAME, "span").text)

            for page in range(1, min(totalPages+1, page_limit)):
                url = f'{self.url}/search/results/people/?keywords=/{name}/&page={page}'
                browser.get(url=url)
                time.sleep(3)

                peoples = browser.find_elements(By.CLASS_NAME, 'reusable-search__result-container')
                
                for people in peoples:
                    button = people.find_element(By.TAG_NAME, 'button')
                    try:
                        buttonText = button.find_element(By.TAG_NAME, 'span').text
                        if buttonText == 'Connect':
                            button.click()
                            SendWithoutNote = browser.find_element(By.XPATH, "//div[@class='artdeco-modal artdeco-modal--layer-default send-invite']//button[2]")
                            SendWithoutNote.click()
                            time.sleep(5)
                    except Exception as e:
                        print("some exception has occured")






            # users = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'org-people-profile-card__profile-card-spacing')))

            # for user in users:
            #     userCardFooter = user.find_element(By.CLASS_NAME, 'ph3')
            #     button = userCardFooter.find_element(By.TAG_NAME, "button")

            #     buttonText = button.find_element(By.TAG_NAME, 'span').text

            #     if buttonText == 'Connect':
            #         button.click()
            #         SendWithoutNote = browser.find_element(By.XPATH, "//div[@class='artdeco-modal artdeco-modal--layer-default send-invite']//button[2]")
            #         SendWithoutNote.click()
            #         time.sleep(5)

        except Exception as e:
            print(e)

    def PeopleConnect(self):
        try:
            df = pd.read_csv('data/m_people.csv')
            self.__login()
            for index, row in df.iterrows():
                name = row['Name']
                self.__PeopleConnect(name)
        except Exception as e:
            print(e)
        