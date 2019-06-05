from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import re


# 运维管理 - 巡线记录 - 操作

class XxjlTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    xxjlBtn = (By.XPATH, '//*[@id="tt1"]//*[text()="巡线记录"]')  # 巡线记录
    firstviewBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[16]/div/div/span[1]')  # 第一条的查看按钮
    closeviewBtn = (By.XPATH, '/html/body/div[8]/div[1]/div[2]/a')  # 关闭查看弹框
    firstdetailBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[16]/div/div/span[3]')  # 第一条的详情按钮
    closedetailBtn = (By.XPATH, '/html/body/div[10]/div[1]/div[2]/a')  # 关闭详情弹框
    pageNum = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]')  # 右下角数据统计
    firstdeleteBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[16]/div/div/span[2]')  # 第一条的删除按钮
    resetBtn = (By.XPATH, '//*[@id="reset"]')  # 重置

    def test_login_zhaobingcheng(self):
        logging.info('=========test_login_zhaobingcheng============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        time.sleep(2)

        self.driver.find_element(*self.ywglBtn).click()
        self.driver.find_element(*self.xxjlBtn).click()
        l.join_iframe()
        time.sleep(1)
        self.driver.find_element(*self.firstviewBtn).click()
        time.sleep(2)
        alert = self.driver.switch_to_alert().accept()
        time.sleep(2)
        self.driver.find_element(*self.closeviewBtn).click()
        self.driver.find_element(*self.firstdetailBtn).click()
        self.driver.find_element(*self.closedetailBtn).click()
        # 删除前数据条数
        be_PageNum = self.driver.find_element(*self.pageNum).text
        be_nums = re.findall(r'\d+\.?', be_PageNum)
        be_num = be_nums[2]
        be_NUM = int(be_num)
        logging.info('删除前共有数据%s条' % be_NUM)
        time.sleep(1)
        self.driver.find_element(*self.firstdeleteBtn).click()
        alert = self.driver.switch_to_alert().accept()
        time.sleep(2)
        alert = self.driver.switch_to_alert().accept()
        time.sleep(2)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        # 删除后数据条数
        af_PageNum = self.driver.find_element(*self.pageNum).text
        af_nums = re.findall(r'\d+\.?', af_PageNum)
        af_num = af_nums[2]
        af_NUM = int(af_num)
        logging.info('删除后共有数据%s条' % af_NUM)
        time.sleep(1)
        try:
            assert af_NUM == be_NUM - 1
            logging.info('===巡线记录删除成功===')
        except:
            logging.info('===巡线记录删除失败===')
            l.getScreenShot('巡线记录删除失败')
        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
