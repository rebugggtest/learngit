from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import random

# 运维管理 - 直埋段信息管理 - 新增 - 删除

class ZmdTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH, '//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    zmdgl = (By.XPATH, '//*[@id="tt1"]//*[text()="直埋段信息管理"]')  # 直埋段信息管理
    first_start_name = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[3]/div/span')  # 第一条起点设施名称
    well_name_input = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[1]/span/input')  # 井名称？
    searchBtn = (By.XPATH, '//*[@id="searchBox"]/div[2]/a[1]')  # 查询
    first_modify = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[15]/div/a[1]')  # 第一条修改
    zmd_length = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[7]/td[4]/span/input')  # 直埋段长度
    submitBtn = (By.XPATH, '//*[@id="win"]/div/div/a[1]/span/span')  # 提交
    first_zmd_length = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[6]/div')  # 第一条直埋段长度

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
        self.driver.find_element(*self.zmdgl).click()
        l.join_iframe()
        time.sleep(3)

        first_start_text = self.driver.find_element(*self.first_start_name).text
        self.driver.find_element(*self.well_name_input).send_keys(first_start_text)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(1)
        search_start_text = self.driver.find_element(*self.first_start_name).text
        try:
            assert first_start_text == search_start_text
            logging.info('直埋段信息管理查询成功')
        except:
            logging.info('直埋段信息管理查询失败')
            l.getScreenShot('直埋段信息管理查询失败')
        self.driver.find_element(*self.first_modify).click()
        time.sleep(1)
        self.driver.find_element(*self.zmd_length).clear()
        zmd_length_num = random.randint(100, 140)
        self.driver.find_element(*self.zmd_length).send_keys(zmd_length_num)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(1)
        first_zmd_text = self.driver.find_element(*self.first_zmd_length).text
        try:
            assert zmd_length_num == int(first_zmd_text)
            logging.info('直埋段信息管理修改成功')
        except:
            logging.info('直埋段信息管理修改失败')
            l.getScreenShot('直埋段信息管理修改失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
