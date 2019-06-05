from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import re

# 商务管理 - 保证金 - 修改

class BzjTest(StartEnd, BaseView):

    swglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="商务管理"]')  # 商务管理
    bzjBtn = (By.XPATH, '//*[@id="tt1"]//*[text()="保证金"]')  # 保证金
    first_xmmc = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[1]/div/span')  # 第一条数据的项目名称
    first_skr = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[2]/div/span')  # 第一条数据的收款人
    first_oa = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[9]/div/span')  # 第一条数据的OA号
    search_xmmc = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[1]/span/input')  # 搜索框-项目名称
    search_skr = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[2]/span/input')  # 搜索框-收款人
    search_oa = (By.XPATH, '//*[@id="searchBox"]/div/div[3]/span/input')  # 搜索框-OA号
    searchBtn = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[5]/a[1]')  # 查询
    modifyBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[12]/div/a[1]')  # 修改
    srk_je = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[3]/td[2]/span/input')  # 金额输入框
    num_je_text = '2333'  # 金额输入
    submitBtn = (By.XPATH, '//*[@id="myFormId"]/table[2]/tbody/tr/td/a[1]/span/span')  # 提交
    get_je = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[3]/div')  # 该条数据的金额
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[5]/a[2]')  # 重置


    def test_login_zhaobingcheng(self):
        logging.info('=========test_login_zhaobingcheng============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        time.sleep(2)

        self.driver.find_element(*self.swglBtn).click()
        self.driver.find_element(*self.bzjBtn).click()
        l.join_iframe()
        time.sleep(1)
        First_xmmc = self.driver.find_element(*self.first_xmmc).text
        First_skr = self.driver.find_element(*self.first_skr).text
        First_oa = self.driver.find_element(*self.first_oa).text
        time.sleep(1)
        self.driver.find_element(*self.search_xmmc).send_keys(First_xmmc)
        self.driver.find_element(*self.search_skr).send_keys(First_skr)
        self.driver.find_element(*self.search_oa).send_keys(First_oa)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.modifyBtn).click()
        self.driver.find_element(*self.srk_je).clear()
        self.driver.find_element(*self.srk_je).send_keys(*self.num_je_text)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(2)
        Num_je = float(self.num_je_text)
        Get_je = self.driver.find_element(*self.get_je).text
        je = re.findall(r'\d+\.?',Get_je)  #用正则修改je格式
        je_num = je[0]+je[1]+je[2]
        num_je = float(je_num)
        time.sleep(1)
        try:
            assert num_je == Num_je
            logging.info('===保证金 金额修改成功===')
        except:
            logging.info('===保证金 金额修改失败===')
            l.getScreenShot('保证金 金额修改失败')
        self.driver.find_element(*self.resetBtn).click()
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
