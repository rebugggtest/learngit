import logging
import time
from daiwei.common.common_fun import Common
from daiwei.common.run_browser import launch_browser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re

class LoginView(Common):

    username_type=(By.ID,'useraccount')
    password_type=(By.ID,'password')
    yzm = (By.ID, 'code')
    loginBtn=(By.XPATH,'/html/body/div/div[2]/div/div[2]/ul/div/div[1]/button')

    login_info = (By.XPATH, '//*[@id="north"]/div[1]/div[2]/p')

    def login_action(self, username, password):

        logging.info('===============login===============')
        logging.info('input username:%s'%username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('input password:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)
        logging.info('input code：1')
        self.driver.find_element(*self.yzm).send_keys('1')
        logging.info('click loginBtn.')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished ')

        logging.info('check_login')
        text = self.driver.find_element(*self.login_info).text
        text1 = re.findall('\w+\.?', text)
        LoginInfo = text1[2]
        try:
            username = LoginInfo
        except NoSuchElementException:
            logging.info('===登录失败===')
            return False
        else:
            logging.info('===登录成功===')
            return True

if __name__ == '__main__':
    driver = launch_browser()