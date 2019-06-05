from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import random

# 运维管理 - 人手井录入 - 查询 - 修改

class RsjlrTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH, '//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    rsjlr = (By.XPATH, '//*[@id="tt1"]//*[text()="人手井录入"]')  # 人手井录入
    first_well_name = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[2]/div/span')  # 第一条井名称
    well_name_input = (By.XPATH, '//*[@id="searchBox"]/div/div[6]/span/input')  # 井名称输入框
    searchBtn = (By.XPATH, '//*[@id="searchBox"]/div/div[9]/a[1]')  # 查询
    first_modifyBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[33]/div/a[1]')  # 修改
    holes = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[4]/td[4]/span/input')  # 管孔数
    submitBtn = (By.XPATH, '//*[@id="myFormId"]/div/a[1]/span/span')  # 提交
    first_hole = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[6]/div')  # 第一条数据的管孔数
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/div/div[9]/a[2]')  # 重置

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
        self.driver.find_element(*self.rsjlr).click()
        l.join_iframe()
        time.sleep(3)

        first_well_text = self.driver.find_element(*self.first_well_name).text
        self.driver.find_element(*self.well_name_input).send_keys(first_well_text)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(2)
        search_well_text = self.driver.find_element(*self.first_well_name).text
        try:
            assert search_well_text == first_well_text
            logging.info('人手井录入查询成功')
        except:
            logging.info('人手井录入查询失败')
            l.getScreenShot('人手井录入查询失败')
        self.driver.find_element(*self.first_modifyBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.holes).clear()
        holes_num = random.randint(1, 5)
        self.driver.find_element(*self.holes).send_keys(holes_num)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.searchBtn).click()
        first_hole_text = self.driver.find_element(*self.first_hole).text
        try:
            assert holes_num == int(first_hole_text)
            logging.info('人手井录入修改成功')
        except:
            logging.info('人手井录入修改失败')
            l.getScreenShot('人手井录入修改失败')
        self.driver.find_element(*self.resetBtn).click()

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()

if __name__ == '__main__':
    unittest.main()