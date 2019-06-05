from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import random

# 运维管理 - 管道段信息管理 - 查询与修改

class GddTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH, '//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    gddgl = (By.XPATH, '//*[@id="tt1"]//*[text()="管道段信息管理"]')  # 管道段信息管理
    province = (By.XPATH, '//*[@id="searchBox"]/ul/li[1]/span')  # 所属省份
    province_select = (By.XPATH, '/html/body/div[4]/div/div')  # 北京市
    city = (By.XPATH, '//*[@id="searchBox"]/ul/li[2]/span')  # 所属市
    city_select = (By.XPATH, '/html/body/div[5]/div/div')  # 北京市
    county = (By.XPATH, '//*[@id="searchBox"]/ul/li[3]/span')  # 区/县
    county_select = (By.XPATH, '/html/body/div[7]/div/div')  # 东城区
    searchBtn = (By.XPATH, '//*[@id="searchBox"]/ul/li[6]/a[1]')  # 查询
    first_modify = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[21]/div/a[1]')  # 第一条修改
    pipeline_length = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[15]/td[4]/span/input')  # 管道长度
    submitBtn = (By.XPATH, '//*[@id="dd"]/div[1]/div/a[1]/span/span')  # 提交
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/ul/li[6]/a[2]')  # 重置
    first_pipeline_length = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[8]/div/span')  # 第一条管道长度

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
        self.driver.find_element(*self.gddgl).click()
        l.join_iframe()
        time.sleep(3)

        self.driver.find_element(*self.province).click()
        self.driver.find_element(*self.province_select).click()
        self.driver.find_element(*self.city).click()
        self.driver.find_element(*self.city_select).click()
        self.driver.find_element(*self.county).click()
        self.driver.find_element(*self.county_select).click()
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.first_modify).click()
        self.driver.find_element(*self.pipeline_length).clear()
        pipeline_num = random.randint(100, 140)
        self.driver.find_element(*self.pipeline_length).send_keys(pipeline_num)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(2)
        first_pipeline_text = self.driver.find_element(*self.first_pipeline_length).text
        try:
            assert pipeline_num == int(first_pipeline_text)
            logging.info('管道段信息管理修改成功')
        except:
            logging.info('管道段信息管理修改失败')
            l.getScreenShot('管道段信息管理修改失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
