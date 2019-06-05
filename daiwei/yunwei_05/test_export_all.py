from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import openpyxl
import unittest
import time
import logging
import re
import os


# 运维管理 - 巡线问题上报 - 导出全部

class XxwtTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH,'//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    xxwtBtn = (By.XPATH,'//*[@id="tt1"]//*[text()="巡线问题上报"]')  # 巡线问题上报
    string = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]')  # 右下角该模块数据条数
    export_all = (By.XPATH, '//*[@id="searchPanel"]/div/div/a[2]')  # 导出全部
    slavepath = r'C:\Users\Ymd\Downloads\巡线问题上报.xlsx'  # 文件全路径

    def test_login_zhaobingcheng(self):
        logging.info('=========test_login_zhaobingcheng============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        time.sleep(2)

        self.driver.find_element(*self.ywglBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.xxwtBtn).click()
        l.join_iframe()
        time.sleep(1)

# 获取该模块数据条数
        string_num = self.driver.find_element(*self.string).text
        nums = re.findall('\d+\.?', string_num)
        num = nums[2]
        NUM = int(num)
        logging.info('当前模块共有数据%s行' % NUM)

# 导出全部数据
        self.driver.find_element(*self.export_all).click()
        time.sleep(3)
        workbook = openpyxl.load_workbook(self.slavepath)  # 读取excel
        sheet = workbook['Sheet1']
        h = sheet.max_row  # 行
        logging.info('导出表数据的行数为%s' % h)
        time.sleep(2)
        try:
            assert NUM == h - 1
            logging.info('巡线问题上报导出全部成功')
        except:
            logging.info('巡线问题上报导出全部失败')
            l.getScreenShot('巡线问题上报导出全部失败')
        os.remove(self.slavepath)  # 删除下载的文件

        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
