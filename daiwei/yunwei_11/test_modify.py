from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import random

# 运维管理 - 接头盒管理 - 查询与修改

class JtglTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH, '//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    jtgl = (By.XPATH, '//*[@id="tt1"]//*[text()="接头盒管理"]')  # 接头盒管理
    first_jth_name = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[1]/div/span')  # 第一条接头盒名称
    jth_name_input = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[6]/span/input')  # 接头盒名称输入框
    searchBtn = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[9]/a[1]')  # 查询
    first_modifyBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[13]/div/a[1]')  # 修改
    longitude = (By.XPATH, '//*[@id="myFormId"]/table/tbody/tr[6]/td[2]/span/input')  # 经度
    submitBtn = (By.XPATH, '//*[@id="win"]/div/div/a[1]/span/span')  # 提交
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[9]/a[2]')  # 重置
    first_longitude = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[7]/div')  # 第一条经度

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
        self.driver.find_element(*self.jtgl).click()
        l.join_iframe()
        time.sleep(3)

        first_jth_text = self.driver.find_element(*self.first_jth_name).text
        self.driver.find_element(*self.jth_name_input).send_keys(first_jth_text)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(2)
        search_jth_text = self.driver.find_element(*self.first_jth_name).text
        try:
            assert first_jth_text == search_jth_text
            logging.info('接头盒管理查询成功')
        except:
            logging.info('接头盒管理查询失败')
            l.getScreenShot('接头盒管理查询失败')
        self.driver.find_element(*self.first_modifyBtn).click()
        self.driver.find_element(*self.longitude).clear()
        longitude_num = random.randint(100, 140)
        self.driver.find_element(*self.longitude).send_keys(longitude_num)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(1)
        first_longitude_text = self.driver.find_element(*self.first_longitude).text
        try:
            assert longitude_num == int(first_longitude_text)
            logging.info('接头盒管理修改成功')
        except:
            logging.info('接头盒管理修改失败')
            l.getScreenShot('接头盒管理修改失败')
        self.driver.find_element(*self.resetBtn).click()

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()