from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import random

# 运维管理 - 杆路段信息管理 - 修改

class GldTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH, '//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    gldgl = (By.XPATH, '//*[@id="tt1"]//*[text()="杆路段信息管理"]')  # 杆路段信息管理
    first_gld_length = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[7]/div/span')  # 第一条杆路段长度
    first_modify = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[18]/div/a[1]')  # 第一条修改
    gld_length = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[14]/td[4]/span/input')  # 杆路段长度
    submitBtn = (By.XPATH, '//*[@id="dd"]/div[1]/div/a[1]/span/span')  # 提交
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/ul[2]/li[3]/a[2]')  # 重置

    def test_login_zhaobingcheng(self):
        logging.info('=========test_login_zhaobingcheng============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        time.sleep(2)

        self.driver.find_element(*self.ywglBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.gxzygl).click()
        time.sleep(2)
        self.driver.find_element(*self.gldgl).click()
        l.join_iframe()
        time.sleep(3)

        self.driver.find_element(*self.first_modify).click()
        time.sleep(1)
        self.driver.find_element(*self.gld_length).clear()
        gld_length_num = random.randint(100, 140)
        self.driver.find_element(*self.gld_length).send_keys(gld_length_num)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(3)
        self.driver.find_element(*self.resetBtn).click()
        first_gld_num = self.driver.find_element(*self.first_gld_length).text
        try:
            assert gld_length_num == int(first_gld_num)
            logging.info('杆路段信息管理修改成功')
        except:
            logging.info('杆路段信息管理修改失败')
            l.getScreenShot('杆路段信息管理修改失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
