from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import re
import random

# 运维管理 - 中继段信息 - 新增 - 删除

class ZjdTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH, '//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    zjdxx = (By.XPATH, '//*[@id="tt1"]//*[text()="中继段信息"]')  # 中继段信息
    addBtn = (By.XPATH, '/html/body/div[1]/div[2]/div/a[1]')  # 新增
    province = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[1]/td[2]/span[1]')  # 所属省份
    province_select = (By.XPATH, '/html/body/div[8]/div/div')  # 北京市
    city = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[1]/td[4]/span[1]')  # 所属市
    city_select = (By.XPATH, '/html/body/div[13]/div/div')  # 北京市
    county = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[3]/td[2]/span')  # 区/县
    county_select = (By.XPATH, '/html/body/div[12]/div/div')  # 东城区
    start_station = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[5]/td[2]/span[1]/input')  # 起始站
    start_station_name = '1'
    start_station_select = (By.XPATH, '/html/body/div[9]/div/div[2]')  # 黑龙江省伊春市伊春区建林街1号
    end_station = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[5]/td[4]/span[1]/input')  # 终点站
    end_station_name = '1'
    end_station_select = (By.XPATH, '/html/body/div[11]/div/div')  # 黑龙江省伊春市伊春区建林街13号
    cable_num = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[7]/td[2]/span[1]/input')  # 光缆芯数
    cable_num_text = '2'
    cable_class = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[7]/td[4]/span[1]')  # 光缆级别
    cable_class_select = (By.XPATH, '/html/body/div[10]/div/div')  # 接入层
    cable_signage = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[9]/td[2]/span[1]/input')  # 光缆标牌
    cable_signage_input = '001'  # 光缆标牌输入
    start_ODF = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[9]/td[4]/span[1]/input')  # 起始点ODF板位
    start_ODF_input = '1'  # 起始点ODF板位输入
    end_ODF = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[11]/td[2]/span[1]/input')  # 终点ODF板位
    end_ODF_input = '2'  # 终点ODF板位输入
    zjd_length = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[27]/td[4]/span[1]/input')  # 中继段长度
    file_select = (By.XPATH, '//*[@id="picturepath"]')  # 选择文件
    slavepath = r'D:\1.jpg'
    submitBtn = (By.XPATH, '//*[@id="dd"]/div[1]/div/a[1]/span/span')  # 提交
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/ul[2]/li/a[2]')  # 重置

    pageNum = (By.XPATH, '//*[@id="tt"]/div[1]/div/div[2]/div[1]')  # 右下角数据统计
    dele_firstBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[32]/div/a[2]')  # 第一条数据的删除按钮
    dele_certainBtn = (By.XPATH, '//*[text()="确定"]')  # 删除的确定

    def test_login_zhaobingcheng(self):
        logging.info('=========test_login_zhaobingcheng============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        time.sleep(2)

        self.driver.find_element(*self.ywglBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.gxzygl).click()
        time.sleep(2)
        self.driver.find_element(*self.zjdxx).click()
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
        self.driver.find_element(*self.province).click()
        self.driver.find_element(*self.province_select).click()
        self.driver.find_element(*self.city).click()
        self.driver.find_element(*self.city_select).click()
        self.driver.find_element(*self.county).click()
        self.driver.find_element(*self.county_select).click()
        self.driver.find_element(*self.start_station).send_keys(*self.start_station_name)
        time.sleep(3)
        self.driver.find_element(*self.start_station_select).click()
        time.sleep(2)
        self.driver.find_element(*self.end_station).send_keys(*self.end_station_name)
        time.sleep(3)
        self.driver.find_element(*self.end_station_select).click()
        self.driver.find_element(*self.cable_num).send_keys(*self.cable_num_text)
        self.driver.find_element(*self.cable_class).click()
        self.driver.find_element(*self.cable_class_select).click()
        self.driver.find_element(*self.cable_signage).send_keys(*self.cable_signage_input)
        self.driver.find_element(*self.start_ODF).send_keys(*self.start_ODF_input)
        self.driver.find_element(*self.end_ODF).send_keys(*self.end_ODF_input)
        time.sleep(1)
        zjd_length_input = random.randint(100, 200)
        self.driver.find_element(*self.zjd_length).send_keys(zjd_length_input)
        self.driver.find_element(*self.file_select).send_keys(*self.slavepath)
        time.sleep(1)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(2)

        af_add_PageNum = self.driver.find_element(*self.pageNum).text
        af_add_nums = re.findall(r'\d+\.?', af_add_PageNum)
        af_add_num = af_add_nums[2]
        af_add_NUM = int(af_add_num)
        logging.info('新增后共有数据%s条' % af_add_NUM)
        time.sleep(1)
        try:
            assert bf_add_NUM == af_add_NUM - 1
            logging.info('中继段信息新增成功')
        except:
            logging.info('中继段信息新增失败')
            l.getScreenShot('中继段信息新增失败')
        time.sleep(1)

        # 删除
        self.driver.find_element(*self.dele_firstBtn).click()
        time.sleep(0.5)
        self.driver.find_element(*self.dele_certainBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(2)
        af_delete_PageNum = self.driver.find_element(*self.pageNum).text
        af_delete_nums = re.findall(r'\d+\.?', af_delete_PageNum)
        af_delete_num = af_delete_nums[2]
        af_delete_NUM = int(af_delete_num)
        logging.info('删除后共有数据%s条' % af_delete_NUM)
        time.sleep(1)
        try:
            assert af_delete_NUM == af_add_NUM - 1
            logging.info('中继段信息删除成功')
        except:
            logging.info('中继段信息删除失败')
            l.getScreenShot('中继段信息删除失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
