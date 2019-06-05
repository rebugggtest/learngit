from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import re

# 运维管理 - 工作量管理（新） - 新工作量数据维护 - 新增 - 删除

class SjwhTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gzlgl = (By.XPATH, '//*[@id="wnav"]/div[2]/div[1]/div[1]')  # 工作量管理（新）
    xgzl_maintain = (By.XPATH, '//*[@id="tt1"]//*[text()="新工作量数据维护"]')  # 新工作量数据维护
    pageNum = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]')  # 右下角数据统计
    addBtn = (By.XPATH, '//*[@id="addId"]')  # 新增
    region = (By.XPATH, '//*[@id="myFormId"]/table/tbody/tr[3]/td[2]/span')  # 大区
    region_select = (By.XPATH, '/html/body/div/div/div')  # 工程管理中心
    operator = (By.XPATH, '//*[@id="carrierOperator"]')  # 运营商
    operator_text = '移动'
    jsms = (By.XPATH, '//*[@id="balanceType"]')  # 结算模式
    jsms_text = '按次'
    profession = (By.XPATH, '//*[@id="profession"]')  # 专业
    profession_text = '集客专线'
    workType = (By.XPATH, '//*[@id="workType"]')  # 工作类别
    workType_text = '应急通信保障'
    measureUnit = (By.XPATH, '//*[@id="units"]')  # 计量单位
    measureUnit_text = '小时'
    modulus = (By.XPATH, '//*[@id="myFormId"]/table/tbody/tr[6]/td[4]/span/input')  # 系数
    modulus_input = '2'
    submitBtn = (By.XPATH, '//*[@id="myFormId"]/table/tbody/tr[7]/td/a[1]')  # 提交
    resetBtn = (By.XPATH, '//*[@id="clean"]')  # 重置

    dele_firstBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[2]/div/a[2]')  # 第一条数据的删除按钮
    dele_certainBtn = (By.XPATH, '//*[text()="确定"]')  # 删除的确定

    first_sele = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[1]/div/input')  # 勾选第1条数据
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

    # 新增
        bf_add_PageNum = self.driver.find_element(*self.pageNum).text
        bf_add_nums = re.findall(r'\d+\.?', bf_add_PageNum)
        bf_add_num = bf_add_nums[2]
        bf_add_NUM = int(bf_add_num)
        logging.info('新增前共有数据%s条' % bf_add_NUM)
        time.sleep(1)

        self.driver.find_element(*self.addBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.operator).send_keys(*self.operator_text)
        self.driver.find_element(*self.jsms).send_keys(*self.jsms_text)
        self.driver.find_element(*self.profession).send_keys(*self.profession_text)
        self.driver.find_element(*self.workType).send_keys(*self.workType_text)
        self.driver.find_element(*self.measureUnit).send_keys(*self.measureUnit_text)
        self.driver.find_element(*self.region).click()
        self.driver.find_element(*self.region_select).click()
        self.driver.find_element(*self.modulus).send_keys(*self.modulus_input)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        af_add_PageNum = self.driver.find_element(*self.pageNum).text
        af_add_nums = re.findall(r'\d+\.?', af_add_PageNum)
        af_add_num = af_add_nums[2]
        af_add_NUM = int(af_add_num)
        logging.info('新增后共有数据%s条' % af_add_NUM)
        time.sleep(1)
        try:
            assert bf_add_NUM == af_add_NUM - 1
            logging.info('新工作量数据维护新增成功')
        except:
            logging.info('新工作量数据维护新增失败')
            l.getScreenShot('新工作量数据维护新增失败')
        time.sleep(1)

    # 删除
        self.driver.find_element(*self.dele_firstBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.dele_certainBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        af_delete_PageNum = self.driver.find_element(*self.pageNum).text
        af_delete_nums = re.findall(r'\d+\.?', af_delete_PageNum)
        af_delete_num = af_delete_nums[2]
        af_delete_NUM = int(af_delete_num)
        logging.info('删除后共有数据%s条' % af_delete_NUM)
        time.sleep(1)
        try:
            assert af_delete_NUM == af_add_NUM - 1
            logging.info('新工作量数据维护删除成功')
        except:
            logging.info('新工作量数据维护删除失败')
            l.getScreenShot('新工作量数据维护删除失败')
        time.sleep(1)

    # 再次新增
        bf_add_PageNum = self.driver.find_element(*self.pageNum).text
        bf_add_nums = re.findall(r'\d+\.?', bf_add_PageNum)
        bf_add_num = bf_add_nums[2]
        bf_add_NUM = int(bf_add_num)
        logging.info('新增前共有数据%s条' % bf_add_NUM)
        time.sleep(1)

        self.driver.find_element(*self.addBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.operator).send_keys(*self.operator_text)
        self.driver.find_element(*self.jsms).send_keys(*self.jsms_text)
        self.driver.find_element(*self.profession).send_keys(*self.profession_text)
        self.driver.find_element(*self.workType).send_keys(*self.workType_text)
        self.driver.find_element(*self.measureUnit).send_keys(*self.measureUnit_text)
        self.driver.find_element(*self.region).click()
        self.driver.find_element(*self.region_select).click()
        self.driver.find_element(*self.modulus).send_keys(*self.modulus_input)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        af_add_PageNum = self.driver.find_element(*self.pageNum).text
        af_add_nums = re.findall(r'\d+\.?', af_add_PageNum)
        af_add_num = af_add_nums[2]
        af_add_NUM = int(af_add_num)
        logging.info('新增后共有数据%s条' % af_add_NUM)
        time.sleep(1)
        try:
            assert bf_add_NUM == af_add_NUM - 1
            logging.info('新工作量数据维护新增成功')
        except:
            logging.info('新工作量数据维护新增失败')
            l.getScreenShot('新工作量数据维护新增失败')
        time.sleep(1)

    # 批量删除
        self.driver.find_element(*self.first_sele).click()
        self.driver.find_element(*self.batch_dele).click()
        time.sleep(1)
        self.driver.find_element(*self.batch_dele_certainBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        af_delete_PageNum = self.driver.find_element(*self.pageNum).text
        af_delete_nums = re.findall(r'\d+\.?', af_delete_PageNum)
        af_delete_num = af_delete_nums[2]
        af_delete_NUM = int(af_delete_num)
        logging.info('批量删除后共有数据%s条' % af_delete_NUM)
        time.sleep(1)
        try:
            assert af_delete_NUM == af_add_NUM - 1
            logging.info('新工作量数据维护批量删除成功')
        except:
            logging.info('新工作量数据维护批量删除失败')
            l.getScreenShot('新工作量数据维护批量删除失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
