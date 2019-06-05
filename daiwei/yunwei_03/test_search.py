from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging


# 运维管理 - 巡线任务查看 - 搜索

class XxrwckTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    xxrwckBtn = (By.XPATH, '//*[@id="tt1"]//*[text()="巡线任务查看"]')  # 巡线任务查看
    firstline_name = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[1]/div/div')  # 第一条的线路名称
    search_linname = (By.XPATH, '//*[@id="keyword"]')  # 模糊搜索输入线路名称
    fuzzy_searchBtn = (By.XPATH, '//*[@id="search"]/span')  # 模糊查询
    exact_search = (By.XPATH, '//*[@id="search1"]/table/tbody/tr/td[6]/input')  # 精确搜索
    resetBtn = (By.XPATH, '//*[@id="resetButton"]/span')  # 重置
    exact_search_input = (By.XPATH, '//*[@id="patrol_route_name"]')  # 精确搜索输入线路名称
    firstline_describe = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[2]/div/div')  # 第一条的线路描述
    line_describe_input = (By.XPATH, '//*[@id="patrol_route_description"]')  # 精确搜索输入线路描述
    exact_searchBtn = (By.XPATH, '//*[@id="advancedSearch"]/span')  # 精确搜索按钮

    def test_login_zhaobingcheng(self):
        logging.info('=========test_login_zhaobingcheng============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        time.sleep(2)

        self.driver.find_element(*self.ywglBtn).click()
        self.driver.find_element(*self.xxrwckBtn).click()
        l.join_iframe()
        time.sleep(1)
        # 模糊搜索
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[@id='myframe']"))  # 切换至frame内嵌的frame
        firstline_text = self.driver.find_element(*self.firstline_name).text  # 模糊搜索前第一条的线路名称
        self.driver.find_element(*self.search_linname).send_keys(firstline_text)
        self.driver.find_element(*self.fuzzy_searchBtn).click()
        firstline_text1 = self.driver.find_element(*self.firstline_name).text  # 模糊搜索后第一条的线路名称
        try:
            assert firstline_text == firstline_text1
            logging.info('巡线任务查看模糊搜索成功')
        except:
            logging.info('巡线任务查看模糊搜索失败')
            l.getScreenShot('巡线任务查看模糊搜索失败')
        time.sleep(1)
        # 精确搜索
        self.driver.find_element(*self.exact_search).click()
        self.driver.find_element(*self.exact_search_input).send_keys(firstline_text)  # 精确搜索输入线路名称
        firstdescribe_text = self.driver.find_element(*self.firstline_describe).text
        self.driver.find_element(*self.line_describe_input).send_keys(firstdescribe_text)
        self.driver.find_element(*self.exact_searchBtn).click()
        firstline_text2 = self.driver.find_element(*self.firstline_name).text  # 精确搜索后第一条的线路名称
        try:
            assert firstline_text == firstline_text2
            logging.info('巡线任务查看精确搜索成功')
        except:
            logging.info('巡线任务查看精确搜索失败')
            l.getScreenShot('巡线任务查看精确搜索失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()

    if __name__ == '__main__':
        unittest.main()
