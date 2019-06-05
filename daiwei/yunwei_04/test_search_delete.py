from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time
import logging
import re

# 运维管理 - 特殊线路管理 - 搜索与删除

class TsxlglTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH,'//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    tsxlBtn = (By.XPATH,'//*[@id="tt1"]//*[text()="特殊线路管理"]')  # 特殊线路管理
    line_name = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[1]/div/div')  # 第一条线路名称
    tsdms = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[5]/div/div')  # 第一条特殊点描述
    tsdmc = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[6]/div/div')  # 第一条特殊点名称
    exact_search = (By.XPATH,'//*[@id="search1"]/ul/li[3]/input')  # 精确搜索
    line_input = (By.XPATH,'//*[@id="routename"]')  # 线路名称
    tsdms_input = (By.XPATH,'//*[@id="special_point_description"]')  # 特殊点描述
    tsdmc_input = (By.XPATH,'//*[@id="special_point_name"]')  # 特殊点名称
    searchBtn = (By.XPATH,'//*[@id="advancedSearch"]')  # 查询
    resetBtn = (By.XPATH, '//*[@id="resetButton"]')  # 重置

    pageNum = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]')  # 右下角数据统计
    dele_firstBtn=(By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[8]/div/div/span[2]')  # 第一条数据的删除按钮

    def test_login_zhaobingcheng(self):
        logging.info('=========test_login_zhaobingcheng============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        time.sleep(2)

        self.driver.find_element(*self.ywglBtn).click()
        WebDriverWait(self.driver, 3).until(lambda x: x.find_element(*self.tsxlBtn))
        self.driver.find_element(*self.tsxlBtn).click()
        l.join_iframe()
# 搜索
        line_text = self.driver.find_element(*self.line_name).text  # 第一条线路名称
        tsdms_text = self.driver.find_element(*self.tsdms).text  # 第一条特殊点描述
        tsdmc_text = self.driver.find_element(*self.tsdmc).text  # 第一条特殊点名称
        self.driver.find_element(*self.exact_search).click()
        self.driver.find_element(*self.line_input).send_keys(line_text)
        self.driver.find_element(*self.tsdms_input).send_keys(tsdms_text)
        self.driver.find_element(*self.tsdmc_input).send_keys(tsdmc_text)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(1)
        af_line_text = self.driver.find_element(*self.line_name).text  # 搜索后第一条线路名称
        try:
            assert line_text == af_line_text
            logging.info('特殊线路管理搜索成功')
        except:
            logging.info('特殊线路管理搜索失败')
            l.getScreenShot('特殊线路管理搜索失败')
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(2)
# 删除
        be_PageNum = self.driver.find_element(*self.pageNum).text
        be_nums = re.findall(r'\d+\.?', be_PageNum)
        be_num = be_nums[2]
        be_NUM = int(be_num)
        logging.info('删除前共有数据%s条' % be_NUM)
        time.sleep(1)
        self.driver.find_element(*self.dele_firstBtn).click()
        time.sleep(1)
        alert = self.driver.switch_to_alert().accept()
        time.sleep(1)
        alert = self.driver.switch_to_alert().accept()
        time.sleep(1)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        af_PageNum = self.driver.find_element(*self.pageNum).text
        af_nums = re.findall(r'\d+\.?', af_PageNum)
        af_num = af_nums[2]
        af_NUM = int(af_num)
        logging.info('删除后共有数据%s条' % af_NUM)
        time.sleep(1)
        try:
            assert af_NUM == be_NUM - 1
            logging.info('特殊线路管理删除成功')
        except:
            logging.info('特殊线路管理删除失败')
            l.getScreenShot('特殊线路管理删除失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
