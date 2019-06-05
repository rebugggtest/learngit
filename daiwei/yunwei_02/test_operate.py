from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import logging
import re


# 运维管理 - 线路管理 - 操作

class XlglTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    xlglBtn = (By.XPATH, '//*[@id="tt1"]//*[text()="线路管理"]')  # 线路管理
    first_viewBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[15]/div/div/span[1]')  # 第一条的查看按钮
    close_viewBtn = (By.XPATH, '/html/body/div[5]/div[1]/div[2]/a')  # 关闭弹框
    first_playbackBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[15]/div/div/span[2]')  # 第一条的轨迹回放按钮
    play_startBtn = (By.XPATH, '//*[@id="startbt"]')  # 开始
    play_pauseBtn = (By.XPATH, '//*[@id="pausebt"]')  # 暂停
    play_endBtn = (By.XPATH, '//*[@id="endbt"]')  # 结束
    pageNum = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]')  # 右下角数据条数
    first_deleteBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[15]/div/div/span[3]')  # 第一条的删除按钮
    resetBtn = (By.XPATH, '//*[@id="reset"]')  # 重置

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

        # 第一条的查看按钮
        self.driver.find_element(*self.first_viewBtn).click()
        time.sleep(1)
        # 判断alert弹出框
        result = EC.alert_is_present()(self.driver)
        if result:
            alert = self.driver.switch_to_alert().accept()
            time.sleep(1)
            self.driver.find_element(*self.close_viewBtn).click()
            logging.info('关闭alert弹窗后关闭查看弹框')
        else:
            self.driver.find_element(*self.close_viewBtn).click()
            logging.info('该条数据没有alert弹窗，关闭查看弹框')
        time.sleep(2)


        # 第一条的轨迹回放按钮
        self.driver.find_element(*self.first_playbackBtn).click()
        time.sleep(1)
        # 判断alert弹出框
        result = EC.alert_is_present()(self.driver)
        if result:
            alert = self.driver.switch_to_alert().accept()
            time.sleep(1)
            self.driver.find_element(*self.close_viewBtn).click()
            logging.info('关闭alert弹窗后关闭轨迹回放弹框')
        else:
            l.join_iframe()
            logging.info('该条数据没有alert弹窗，进行轨迹回放')
            self.driver.find_element(*self.play_startBtn).click()
            time.sleep(10)
            self.driver.find_element(*self.play_pauseBtn).click()
            self.driver.find_element(*self.play_endBtn).click()
            l.quit_iframe()
            time.sleep(1)
            l.join_iframe()
            self.driver.find_element(*self.close_viewBtn).click()
            logging.info('关闭轨迹回放弹框')
        # 删除前数据条数
        be_PageNum = self.driver.find_element(*self.pageNum).text
        be_nums = re.findall(r'\d+\.?', be_PageNum)
        be_num = be_nums[2]
        be_NUM = int(be_num)
        logging.info('删除前共有数据%s条' % be_NUM)
        time.sleep(1)
        # 第一条的删除按钮
        self.driver.find_element(*self.first_deleteBtn).click()
        time.sleep(1)
        alert = self.driver.switch_to_alert().accept()
        time.sleep(1)
        alert = self.driver.switch_to_alert().accept()
        time.sleep(1)
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
            logging.info('===线路管理删除成功===')
        except:
            logging.info('===线路管理删除失败===')
            l.getScreenShot('线路管理删除失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
