from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging

# 运维管理 - 工作量管理（新） - 新工作量详单 - 事件工作量查询 - 搜索

class XdTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gzlgl = (By.XPATH, '//*[@id="wnav"]/div[2]/div[1]/div[1]')  # 工作量管理（新）
    xgzl_detailedList = (By.XPATH, '//*[@id="tt1"]//*[text()="新工作量详单"]')  # 新工作量详单
    first_gzlNum = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[2]/div/span')  # 第一条工作量编号
    gzl_num_searchInput = (By.XPATH, '//*[@id="searchBox"]/ul/li[1]/span/input')  # 工作量编号搜索框
    searchBtn = (By.XPATH, '//*[@id="query"]')  # 查询
    display = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[2]/div[1]')  # 右下角显示
    display_text = '显示1到1,共1记录'

    def test_login_zhaobingcheng(self):
        logging.info('=========test_login_zhaobingcheng============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        time.sleep(2)

        self.driver.find_element(*self.ywglBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.gzlgl).click()
        time.sleep(2)
        self.driver.find_element(*self.xgzl_detailedList).click()
        l.join_iframe()
        time.sleep(3)

        first_gzl_text = self.driver.find_element(*self.first_gzlNum).text
        self.driver.find_element(*self.gzl_num_searchInput).send_keys(first_gzl_text)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(2)
        afSearch_gzlNum = self.driver.find_element(*self.first_gzlNum).text
        displayText = self.driver.find_element(*self.display).text
        try:
            assert first_gzl_text == afSearch_gzlNum and displayText == self.display_text
            logging.info('事件工作量查询成功')
        except:
            logging.info('事件工作量查询失败')
            l.getScreenShot('事件工作量查询失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
