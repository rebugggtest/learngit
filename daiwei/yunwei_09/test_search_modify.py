from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import random

# 运维管理 - 挂墙管理 - 搜索与修改

class GqglTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH, '//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    gqgl = (By.XPATH, '//*[@id="tt1"]//*[text()="挂墙管理"]')  # 挂墙管理
    first_gq_name = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[5]/div/span')  # 第一条挂墙名称
    gq_name_input = (By.XPATH, '//*[@id="searchBox"]/ul[1]/li[6]/span/input')  # 挂墙名称输入框
    searchBtn = (By.XPATH, '//*[@id="searchBox"]/ul[2]/li[3]/a[1]')  # 查询
    first_modifyBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[14]/div/a[1]')  # 修改
    height = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[17]/td[2]/span[1]/input')  # 高度
    submitBtn = (By.XPATH, '//*[@id="dd"]/div/div/a[1]/span/span')  # 提交
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/ul[2]/li[3]/a[2]')  # 重置
    first_height = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[10]/div/span')  # 第一条高度

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
        self.driver.find_element(*self.gqgl).click()
        l.join_iframe()
        time.sleep(3)
        first_gq_text = self.driver.find_element(*self.first_gq_name).text
        self.driver.find_element(*self.gq_name_input).send_keys(first_gq_text)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(2)
        search__gq_text = self.driver.find_element(*self.first_gq_name).text
        try:
            assert first_gq_text == search__gq_text
            logging.info('挂墙管理查询成功')
        except:
            logging.info('挂墙管理查询失败')
            l.getScreenShot('挂墙管理查询失败')
        self.driver.find_element(*self.first_modifyBtn).click()
        self.driver.find_element(*self.height).clear()
        height_num = random.randint(10, 20)
        self.driver.find_element(*self.height).send_keys(height_num)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(1)
        first_height_text = self.driver.find_element(*self.first_height).text
        try:
            assert height_num == int(first_height_text)
            logging.info('挂墙管理修改成功')
        except:
            logging.info('挂墙管理修改失败')
            l.getScreenShot('挂墙管理修改失败')
        self.driver.find_element(*self.resetBtn).click()

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()