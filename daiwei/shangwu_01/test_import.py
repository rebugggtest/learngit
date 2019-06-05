from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import re

# 商务管理 - 标书费 - 导入

class BsfTest(StartEnd, BaseView):

    swglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="商务管理"]')  # 商务管理
    bsfBtn = (By.XPATH, '//*[@id="tt1"]//*[text()="标书费"]')  # 标书费



    def test_login_zhaobingcheng(self):
        logging.info('=========test_login_zhaobingcheng============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        time.sleep(2)

        self.driver.find_element(*self.swglBtn).click()
        self.driver.find_element(*self.bsfBtn).click()
        l.join_iframe()
        time.sleep(1)
# 导出模板并写入内容
        500












        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
