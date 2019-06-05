from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging

# 运维管理 - 采集路线点管理 - 搜索

class CjlxdglTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH,'//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    cjlxBtn = (By.XPATH,'//*[@id="tt1"]//*[text()="采集路线点管理"]')  # 采集路线点管理
    first_xlbsf = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[2]/div')  # 获取第一条数据的线路标示符
    search_input = (By.XPATH,'//*[@id="keyword"]')  # 查询内容
    searchBtn = (By.XPATH,'//*[@id="search"]')  # 查询
    resetBtn = (By.XPATH, '//*[@id="search1"]/ul/li[2]/a[2]')  # 重置


    def test_login_zhaobingcheng(self):
        logging.info('=========test_login_zhaobingcheng============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        time.sleep(2)

        self.driver.find_element(*self.ywglBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.cjlxBtn).click()
        l.join_iframe()
# 搜索
        be_xlbsf_text = self.driver.find_element(*self.first_xlbsf).text  # 获取第一条数据的线路标示符
        self.driver.find_element(*self.search_input).send_keys(be_xlbsf_text)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(10)
        af_xlbsf_text = self.driver.find_element(*self.first_xlbsf).text  # 获取搜索后第一条数据的线路标示符
        try:
            assert be_xlbsf_text == af_xlbsf_text
            logging.info('采集路线点管理搜索成功')
        except:
            logging.info('采集路线点管理搜索失败')
            l.getScreenShot('采集路线点管理搜索失败')
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(3)

        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
