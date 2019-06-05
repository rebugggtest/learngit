from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import random

# 运维管理 - 标石录入 - 查询与修改

class BslrTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH, '//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    bslr = (By.XPATH, '//*[@id="tt1"]//*[text()="标石录入"]')  # 标石录入
    first_bs_name = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[2]/div/span')  # 第一条标石名称
    bs_name_input = (By.XPATH, '//*[@id="searchBox"]/ul[1]/li[6]/span/input')  # 标石名称输入框
    searchBtn = (By.XPATH, '//*[@id="searchBox"]/ul[2]/li[3]/a[1]')  # 查询
    first_modifyBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[16]/div/a[1]')  # 修改
    cable_depth = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[21]/td[2]/span[1]/input')  # 光缆埋深
    submitBtn = (By.XPATH, '//*[@id="dd"]/div/div/a[1]/span/span')  # 提交
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/ul[2]/li[3]/a[2]')  # 重置
    first_cable_depth = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[12]/div/span')  # 第一条光缆埋深


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
        self.driver.find_element(*self.bslr).click()
        l.join_iframe()
        time.sleep(3)

        first_bs_text = self.driver.find_element(*self.first_bs_name).text
        self.driver.find_element(*self.bs_name_input).send_keys(first_bs_text)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(2)
        search_bs_text = self.driver.find_element(*self.first_bs_name).text
        try:
            assert first_bs_text == search_bs_text
            logging.info('标石录入查询成功')
        except:
            logging.info('标石录入查询失败')
            l.getScreenShot('标石录入查询失败')
        self.driver.find_element(*self.first_modifyBtn).click()
        self.driver.find_element(*self.cable_depth).clear()
        depth_num = random.randint(30, 50)
        self.driver.find_element(*self.cable_depth).send_keys(depth_num)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(1)
        first_cable_text = self.driver.find_element(*self.first_cable_depth).text
        try:
            assert depth_num == int(first_cable_text)
            logging.info('标石录入修改成功')
        except:
            logging.info('标石录入修改失败')
            l.getScreenShot('标石录入修改失败')
        self.driver.find_element(*self.resetBtn).click()

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()