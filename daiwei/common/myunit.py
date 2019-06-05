import unittest
import logging
from daiwei.common.run_browser import launch_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class StartEnd(unittest.TestCase):

    username_type=(By.ID,'useraccount')  # 账号输入框

    csv_file = '../data/account.csv'

    def setUp(self):
        logging.info('======setUp=========')
        self.driver = launch_browser()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        logging.info('======tearDown=====')
        WebDriverWait(self.driver, 7).until(lambda x: x.find_element(*self.username_type))
        self.driver.quit()

if __name__ == '__main__':
    driver = launch_browser()
