from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import random

# 运维管理 - 电杆录入 - 查询 - 修改

class DglrTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH,'//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH,'//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    dglr = (By.XPATH,'//*[@id="tt1"]//*[text()="电杆录入"]')  # 电杆录入
    first_pole_name = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[2]/div/span')  # 第一条电杆名称
    first_pole_height = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[14]/div')  # 第一条电杆高度
    pole_name_input = (By.XPATH,'//*[@id="searchBox"]/ul[2]/li[1]/span/input')  # 电杆名称输入框
    searchBtn = (By.XPATH,'//*[@id="searchBox"]/ul[2]/li[4]/a[1]')  # 查询
    modifyBtn = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[19]/div/a[1]')  # 修改
    pole_height = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[7]/td[4]/span[1]/input')  # 电杆高度
    submitBtn = (By.XPATH,'//*[@id="dd"]/div/div/a[1]/span/span')  # 提交
    resetBtn = (By.XPATH,'//*[@id="searchBox"]/ul[2]/li[4]/a[2]')  # 重置

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
        self.driver.find_element(*self.dglr).click()
        l.join_iframe()
        time.sleep(1)

        first_pole_text = self.driver.find_element(*self.first_pole_name).text
        self.driver.find_element(*self.pole_name_input).send_keys(first_pole_text)
        self.driver.find_element(*self.searchBtn).click()
        search_pole_text = self.driver.find_element(*self.first_pole_name).text
        try:
            assert search_pole_text == first_pole_text
            logging.info('电杆录入查询成功')
        except:
            logging.info('电杆录入查询失败')
            l.getScreenShot('电杆录入查询失败')
        time.sleep(2)
        self.driver.find_element(*self.modifyBtn).click()
        self.driver.find_element(*self.pole_height).clear()
        num = random.randint(5, 15)
        self.driver.find_element(*self.pole_height).send_keys(num)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.searchBtn).click()
        pole_height = self.driver.find_element(*self.first_pole_height).text
        try:
            assert num == int(pole_height)
            logging.info('电杆录入修改成功')
        except:
            logging.info('电杆录入修改失败')
            l.getScreenShot('电杆录入修改失败')
        time.sleep(2)
        self.driver.find_element(*self.resetBtn).click()

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
