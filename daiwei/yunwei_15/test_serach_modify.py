from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import random

# 运维管理 - 中继段信息 - 修改

class ZjdTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH, '//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    zjdxx = (By.XPATH, '//*[@id="tt1"]//*[text()="中继段信息"]')  # 中继段信息
    first_cable_num = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[9]/div/span')  # 第一条光缆芯数
    first_modify = (By.XPATH, '//*[@id="datagrid-row-r1-2-1"]/td[32]/div/a[1]')  # 第一条修改
    cable_num = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[7]/td[2]/span[1]/input')  # 光缆芯数
    submitBtn = (By.XPATH, '//*[@id="dd"]/div[1]/div/a[1]/span/span')  # 提交
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/ul[2]/li/a[2]')  # 重置

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
        self.driver.find_element(*self.zjdxx).click()
        l.join_iframe()
        time.sleep(3)

        self.driver.find_element(*self.first_modify).click()
        time.sleep(1)
        self.driver.find_element(*self.cable_num).clear()
        cable_NUM = random.randint(50, 100)
        self.driver.find_element(*self.cable_num).send_keys(cable_NUM)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(3)
        self.driver.find_element(*self.resetBtn).click()
        cable_num_text = self.driver.find_element(*self.first_cable_num).text
        try:
            assert cable_NUM == int(cable_num_text)
            logging.info('中继段信息修改成功')
        except:
            logging.info('中继段信息修改失败')
            l.getScreenShot('中继段信息修改失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
