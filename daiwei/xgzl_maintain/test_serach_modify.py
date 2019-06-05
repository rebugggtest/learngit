from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import random

# 运维管理 - 工作量管理（新） - 新工作量数据维护 - 修改

class SjwhTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gzlgl = (By.XPATH, '//*[@id="wnav"]/div[2]/div[1]/div[1]')  # 工作量管理（新）
    xgzl_maintain = (By.XPATH, '//*[@id="tt1"]//*[text()="新工作量数据维护"]')  # 新工作量数据维护
    first_modify = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[2]/div/a[1]')  # 第一条数据的修改
    modulus_input = (By.XPATH, '//*[@id="myFormId"]/table/tbody/tr[6]/td[4]/span/input')  # 系数
    submitBtn = (By.XPATH, '//*[@id="myFormId"]/table/tbody/tr[7]/td/a[1]')  # 提交
    resetBtn = (By.XPATH, '//*[@id="clean"]')  # 重置
    first_modulus = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[10]/div')  # 第一条数据的系数

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
        self.driver.find_element(*self.xgzl_maintain).click()
        l.join_iframe()
        time.sleep(3)

        self.driver.find_element(*self.first_modify).click()
        self.driver.find_element(*self.modulus_input).clear()
        modulus_num = random.randint(5, 20)
        time.sleep(3)
        self.driver.find_element(*self.modulus_input).send_keys(modulus_num)
        time.sleep(1)
        self.driver.find_element(*self.submitBtn).click()
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        first_modulus_text = self.driver.find_element(*self.first_modulus).text
        time.sleep(1)
        try:
            assert modulus_num == int(float(first_modulus_text))
            logging.info('新工作量数据维护修改成功')
        except:
            logging.info('新工作量数据维护修改失败')
            l.getScreenShot('新工作量数据维护修改失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
