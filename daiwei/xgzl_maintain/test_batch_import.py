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

# 运维管理 - 工作量管理（新） - 新工作量数据维护 - 批量导入

class SjwhTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gzlgl = (By.XPATH, '//*[@id="wnav"]/div[2]/div[1]/div[1]')  # 工作量管理（新）
    xgzl_maintain = (By.XPATH, '//*[@id="tt1"]//*[text()="新工作量数据维护"]')  # 新工作量数据维护
    string = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]')  # 右下角该模块数据条数
    importBtn = (By.XPATH, '//*[@id="importId"]')  # 批量导入
    download = (By.XPATH, '//*[@id="win"]/div[2]/a/span/span')  # 下载模板
    slavepath = r'C:\Users\Ymd\Downloads\工作量数据维护导入模板.xlsx'  # 文件全路径
    A = '工程管理中心'
    row2 = '测试2'
    row3 = '测试3'
    row4 = '测试4'
    cell_H = '3'
    file_select = (By.XPATH, '//*[@id="FormUpdate"]/div/span/a')  # 点击选择文件
    submitBtn = (By.XPATH, '//*[@id="win"]/div[3]/a[1]/span/span')  # 提交
    close_alert = (By.XPATH, '/html/body/div[10]/div[1]/div[2]/a')  # 关闭提示信息
    resetBtn = (By.XPATH, '//*[@id="clean"]')  # 重置

    region_search = (By.XPATH, '//*[@id="searchBox"]/ul/li[1]/span')  # 大区搜索框
    region_search_select = (By.XPATH, '/html/body/div[3]/div/div')  # 工程管理中心
    searchBtn = (By.XPATH, '//*[@id="query"]')  # 查询
    first_operator = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[4]/div/span')  # 第一条运营商
    second_operator = (By.XPATH, '//*[@id="datagrid-row-r1-2-1"]/td[4]/div/span')  # 第二条运营商
    third_operator = (By.XPATH, '//*[@id="datagrid-row-r1-2-2"]/td[4]/div/span')  # 第三条运营商

    first_select = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[1]/div/input')  # 勾选第1条数据
    second_select = (By.XPATH, '//*[@id="datagrid-row-r1-2-1"]/td[1]/div/input')  # 勾选第2条数据
    third_select = (By.XPATH, '//*[@id="datagrid-row-r1-2-2"]/td[1]/div/input')  # 勾选第3条数据

    batch_dele = (By.XPATH, '//*[@id="tool"]/div/div/a[2]')  # 批量删除
    batch_dele_certainBtn = (By.XPATH, '//*[text()="确定"]')  # 批量删除的确定

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
        sheet['A2'] = sheet['A3'] = sheet['A4'] = self.A
        sheet['B2'] = sheet['C2'] = sheet['D2'] = sheet['E2'] = sheet['F2'] = self.row2
        sheet['B3'] = sheet['C3'] = sheet['D3'] = sheet['E3'] = sheet['F3'] = self.row3
        sheet['B4'] = sheet['C4'] = sheet['D4'] = sheet['E4'] = sheet['F4'] = self.row4
        sheet['H2'] = sheet['H3'] = sheet['H4'] = self.cell_H

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

    # 获取导入3条数据后该模块数据条数
        af_string_num = self.driver.find_element(*self.string).text
        af_nums = re.findall('\d+\.?', af_string_num)
        af_num = af_nums[2]
        af_NUM = int(af_num)
        logging.info('导入后当前页共有数据%s条' % af_NUM)
        time.sleep(1)
        try:
            assert af_NUM == be_NUM + 3
            logging.info('新工作量数据维护批量导入成功')
        except:
            logging.info('新工作量数据维护批量导入失败')
            l.getScreenShot('新工作量数据维护批量导入失败')
        time.sleep(1)

    #判断批量导入的数据内容
        self.driver.find_element(*self.region_search).click()
        self.driver.find_element(*self.region_search_select).click()
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(1)
        first_operator_text = self.driver.find_element(*self.first_operator).text
        second_operator_text = self.driver.find_element(*self.second_operator).text
        third_operator_text = self.driver.find_element(*self.third_operator).text
        time.sleep(1)
        try:
            assert first_operator_text == self.row2 and second_operator_text == self.row3 \
                    and third_operator_text == self.row4
            logging.info('新工作量数据维护批量导入成功')
        except:
            logging.info('新工作量数据维护批量导入失败')
            l.getScreenShot('新工作量数据维护批量导入失败')
        time.sleep(1)

    #批量删除导入的数据
        self.driver.find_element(*self.first_select).click()
        self.driver.find_element(*self.second_select).click()
        self.driver.find_element(*self.third_select).click()

        self.driver.find_element(*self.batch_dele).click()
        self.driver.find_element(*self.batch_dele_certainBtn).click()
        time.sleep(1)
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
