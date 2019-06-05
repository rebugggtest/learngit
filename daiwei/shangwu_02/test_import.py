from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time
import logging
import openpyxl
import re
import os

# 商务管理 - 保证金 - 导入

class BzjTest(StartEnd, BaseView):

    swglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="商务管理"]')  # 商务管理
    bzjBtn = (By.XPATH, '//*[@id="tt1"]//*[text()="保证金"]')  # 保证金
    text_smmc = '赵炳成001'
    text_skr = '赵炳成002'
    text_OA = '借-20181119'
    string = (By.XPATH, '//*[@id="tt"]/div[1]/div/div[3]/div[1]')  # 右下角该模块数据条数
    importBtn = (By.XPATH, '//*[@id="searchBox"]/div[2]/div/a[3]')  # 导入
    download = (By.XPATH, '//*[@id="win"]/div[2]/a/span/span')  # 下载模板
    slavepath = r'C:\Users\Ymd\Downloads\保证金导入模板.xlsx'  # 文件全路径
    file_select = (By.XPATH, '//*[@id="FormUpdate"]/div/span/a/label')  # 点击选择文件
    submitBtn = (By.XPATH, '//*[@id="win"]/div[3]/a[1]/span/span')  # 提交
    close_alert = (By.XPATH, '/html/body/div[5]/div[1]/div[2]/a')  # 关闭提示信息
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[5]/a[2]')  # 重置
    smmc = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[1]/span/input')  # 项目名称
    skr = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[2]/span/input')  # 收款人
    OA = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[3]/span/input')  # OA账号
    searchBtn = (By.XPATH, '//*[@id="searchBox"]/div[1]/div[5]/a[1]')  # 查询
    deleteBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[12]/div/a[2]')  # 删除
    certain = (By.XPATH, '/html/body/div[5]/div[3]/a[1]/span/span')  # 确定



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
# 获取该模块数据条数
        be_string_num = self.driver.find_element(*self.string).text
        be_nums = re.findall('\d+\.?', be_string_num)
        be_num = be_nums[2]
        be_NUM = int(be_num)
        logging.info('导入前当前页共有数据%s条' % be_NUM)

# 导出模板并写入内容
        self.driver.find_element(*self.importBtn).click()
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.download))
        self.driver.find_element(*self.download).click()
        time.sleep(2)
        workbook = openpyxl.load_workbook(self.slavepath)  # 读取excel
        sheet = workbook['Sheet1']

        # 写入实际内容（第二行）
        logging.info("系统即将执行Excel写入...")
        sheet['A2'] = self.text_smmc
        sheet['B2'] = self.text_skr
        sheet['C2'] = '111.11'
        sheet['D2'] = '2018-11-19'
        sheet['E2'] = '2018-11-20'
        sheet['F2'] = '100.00'
        sheet['G2'] = '13655554444'
        sheet['H2'] = '1'
        sheet['I2'] = self.text_OA
        sheet['J2'] = '1'
        sheet['K2'] = '111'

        workbook.save(self.slavepath)  # 保存
        logging.info("写入完成，即将上传")
        self.driver.find_element(*self.file_select).click()
        time.sleep(2)
        l.win32_pick_slave(self.slavepath)
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.submitBtn))
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.close_alert).click()
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(2)
# 获取导入一条数据后该模块数据条数
        af_string_num = self.driver.find_element(*self.string).text
        af_nums = re.findall('\d+\.?', af_string_num)
        af_num = af_nums[2]
        af_NUM = int(af_num)
        logging.info('导入后当前页共有数据%s条' % af_NUM)
        time.sleep(1)
        try:
            assert af_NUM == be_NUM + 1
            logging.info('===保证金导入成功===')
        except:
            logging.info('===保证金导入失败===')
            l.getScreenShot('保证金导入失败')
        time.sleep(1)

#删除该导入数据
        self.driver.find_element(*self.smmc).send_keys(self.text_smmc)
        self.driver.find_element(*self.skr).send_keys(self.text_skr)
        self.driver.find_element(*self.OA).send_keys(self.text_OA)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.deleteBtn).click()
        self.driver.find_element(*self.certain).click()
        time.sleep(2)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        string_num = self.driver.find_element(*self.string).text
        nums = re.findall('\d+\.?', string_num)
        num = nums[2]
        NUM = int(num)
        logging.info('删除后当前页共有数据%s条' % NUM)
        time.sleep(1)
        try:
            assert NUM == be_NUM
            logging.info('===导入数据删除成功===')
        except:
            logging.info('===导入数据删除失败===')
            l.getScreenShot('导入数据删除失败')
        time.sleep(1)

        os.remove(self.slavepath)

        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
