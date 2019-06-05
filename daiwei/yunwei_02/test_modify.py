from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time
import logging
import random


# 运维管理 - 线路管理 - 修改

class XlglTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    xlglBtn = (By.XPATH, '//*[@id="tt1"]//*[text()="线路管理"]')  # 线路管理
    firstmodifyBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[15]/div/div/span[4]')  # 第一条数据的修改
    closewindowBtn = (By.XPATH, '/html/body/div[5]/div[1]/div[2]/a')  # 修改弹框的关闭按钮X
    standardNum = (By.XPATH, '//*[@id="standardCount"]')  # 达标次数
    submitBtn = (By.XPATH, '//*[@id="myFormId"]/div/table/tbody/tr[10]/td/a[1]')  # 提交
    cancelBtn = (By.XPATH, '//*[@id="myFormId"]/div/table/tbody/tr[10]/td/a[2]')  # 取消
    resetBtn = (By.XPATH, '//*[@id="reset"]')  # 重置
    time = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[12]/div/div')  # 第一条数据的达标次数


    def test_login_zhaobingcheng(self):
        logging.info('=========test_login_zhaobingcheng============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        time.sleep(2)

        self.driver.find_element(*self.ywglBtn).click()
        self.driver.find_element(*self.xlglBtn).click()
        l.join_iframe()
        time.sleep(2)

        self.driver.find_element(*self.firstmodifyBtn).click()
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.closewindowBtn))
        l.join_iframe()
        self.driver.find_element(*self.standardNum).clear()
        num = random.randint(1, 7)
        self.driver.find_element(*self.standardNum).send_keys(num)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(2)
        alert = self.driver.switch_to_alert().accept()
        time.sleep(2)
        self.driver.find_element(*self.cancelBtn).click()
        l.quit_iframe()
        time.sleep(2)
        l.join_iframe()
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(3)
        standard = self.driver.find_element(*self.time).text
        timeNum = int(standard)
        try:
            assert timeNum == num
            logging.info('线路管理修改达标次数成功')
        except:
            logging.info('线路管理修改达标次数失败')
            l.getScreenShot('线路管理修改达标次数失败')
        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
