from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import re

# 运维管理 - 直埋段信息管理 - 新增 - 删除

class ZmdTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH, '//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    zmdgl = (By.XPATH, '//*[@id="tt1"]//*[text()="直埋段信息管理"]')  # 直埋段信息管理
    addBtn = (By.XPATH, '//*[@id="addId"]')  # 新增
    zm_class = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[1]/td[2]/span')  # 直埋级别
    zm_class_select = (By.XPATH, '/html/body/div[16]/div/div')  # 省际干线
    property_nature = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[1]/td[4]/span')  # 产权性质
    property_nature_select = (By.XPATH, '/html/body/div[17]/div/div')  # 自建
    province = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[2]/td[2]/span[1]')  # 所属省份
    province_select = (By.XPATH, '/html/body/div[13]/div/div')  # 北京市
    city = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[2]/td[4]/span[1]')  # 所属市
    city_select = (By.XPATH, '/html/body/div[22]/div/div')  # 北京市
    county = (By.XPATH, '//*[@id="td5"]/span')  # 区/县
    county_select = (By.XPATH, '/html/body/div[21]/div/div')  # 东城区
    maintain_mode = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[3]/td[4]/span')  # 维护方式
    maintain_mode_select = (By.XPATH, '/html/body/div[18]/div/div')  # 综合代维

    start_type = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[4]/td[2]/span[1]')  # 起点设施类型
    start_type_select = (By.XPATH, '/html/body/div[14]/div/div[2]')  # 人手井
    end_type = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[4]/td[4]/span[1]')  # 终点设施类型
    end_type_select = (By.XPATH, '/html/body/div[15]/div/div[2]')  # 人手井
    start_name = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[5]/td[2]/span[1]')  # 起点设施名称
    start_name_select = (By.XPATH, '//*[text()="222测试"]')  # 222测试
    end_name = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[5]/td[4]/span[1]')  # 终点设施名称
    end_name_select = (By.XPATH, '/html/body/div[24]/div//*[text()="333测试"]')  # 333测试
    share_unit = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[6]/td[2]/span[1]')  # 共享单位
    share_unit_select = (By.XPATH, '/html/body/div[19]/div/div[2]')  # 电信
    co_unit = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[6]/td[4]/span[1]')  # 共建单位
    co_unit_select = (By.XPATH, '/html/body/div[20]/div/div[2]')  # 电信
    submitBtn = (By.XPATH, '//*[@id="win"]/div/div/a[1]/span/span')  # 提交
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/div[2]/a[2]')  # 重置

    pageNum = (By.XPATH, '/html/body/div[1]/div/div[3]/div[1]')  # 右下角数据统计
    dele_firstBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[15]/div/a[2]')  # 第一条数据的删除按钮
    dele_certainBtn = (By.XPATH, '//*[text()="确定"]')  # 删除的确定

    show_data = (By.CSS_SELECTOR, 'select.pagination-page-list')  # 显示数据条数
    show_data_select = (By.CSS_SELECTOR, 'select.pagination-page-list>option:nth-child(3)')  # 20
    select_ten = (By.XPATH, '//*[@id="datagrid-row-r1-1-9"]/td[2]/div/input')  # 勾选第10条数据
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
        self.driver.find_element(*self.gxzygl).click()
        time.sleep(2)
        self.driver.find_element(*self.zmdgl).click()
        l.join_iframe()
        time.sleep(3)

        bf_add_PageNum = self.driver.find_element(*self.pageNum).text
        bf_add_nums = re.findall(r'\d+\.?', bf_add_PageNum)
        bf_add_num = bf_add_nums[2]
        bf_add_NUM = int(bf_add_num)
        logging.info('新增前共有数据%s条' % bf_add_NUM)
        time.sleep(1)

    # 新增
        self.driver.find_element(*self.addBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.zm_class).click()
        self.driver.find_element(*self.zm_class_select).click()
        self.driver.find_element(*self.property_nature).click()
        self.driver.find_element(*self.property_nature_select).click()
        self.driver.find_element(*self.province).click()
        self.driver.find_element(*self.province_select).click()
        self.driver.find_element(*self.city).click()
        self.driver.find_element(*self.city_select).click()
        self.driver.find_element(*self.county).click()
        self.driver.find_element(*self.county_select).click()
        self.driver.find_element(*self.maintain_mode).click()
        self.driver.find_element(*self.maintain_mode_select).click()
        self.driver.find_element(*self.start_type).click()
        self.driver.find_element(*self.start_type_select).click()
        self.driver.find_element(*self.end_type).click()
        self.driver.find_element(*self.end_type_select).click()
        self.driver.find_element(*self.start_name).click()
        time.sleep(1)
        self.driver.find_element(*self.start_name_select).click()
        self.driver.find_element(*self.end_name).click()
        time.sleep(1)
        self.driver.find_element(*self.end_name_select).click()
        self.driver.find_element(*self.share_unit).click()
        self.driver.find_element(*self.share_unit_select).click()
        self.driver.find_element(*self.co_unit).click()
        self.driver.find_element(*self.co_unit_select).click()
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
            logging.info('直埋段信息管理新增成功')
        except:
            logging.info('直埋段信息管理新增失败')
            l.getScreenShot('直埋段信息管理新增失败')
        time.sleep(1)

    # 删除
        self.driver.find_element(*self.dele_firstBtn).click()
        time.sleep(0.5)
        self.driver.find_element(*self.dele_certainBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(5)
        af_delete_PageNum = self.driver.find_element(*self.pageNum).text
        af_delete_nums = re.findall(r'\d+\.?', af_delete_PageNum)
        af_delete_num = af_delete_nums[2]
        af_delete_NUM = int(af_delete_num)
        logging.info('删除后共有数据%s条' % af_delete_NUM)
        time.sleep(1)
        try:
            assert af_delete_NUM == af_add_NUM - 1
            logging.info('直埋段信息管理删除成功')
        except:
            logging.info('直埋段信息管理删除失败')
            l.getScreenShot('直埋段信息管理删除失败')
        time.sleep(1)

    # 批量删除
        self.driver.find_element(*self.show_data).click()
        time.sleep(1)
        self.driver.find_element(*self.show_data_select).click()
        time.sleep(3)
        self.driver.find_element(*self.select_ten).click()
        self.driver.find_element(*self.batch_dele).click()
        time.sleep(1)
        self.driver.find_element(*self.batch_dele_certainBtn).click()
        time.sleep(3)  # 批量删除重复操作才可以真正删除
        self.driver.find_element(*self.select_ten).click()
        self.driver.find_element(*self.batch_dele).click()
        time.sleep(1)
        self.driver.find_element(*self.batch_dele_certainBtn).click()
        time.sleep(3)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(5)
        af_batchdele = self.driver.find_element(*self.pageNum).text
        af_batchdele_nums = re.findall(r'\d+\.?', af_batchdele)
        af_batchdele_num = af_batchdele_nums[2]
        af_batchdele_NUM = int(af_batchdele_num)
        logging.info('批量删除后共有数据%s条' % af_batchdele_NUM)
        time.sleep(1)
        try:
            assert af_batchdele_NUM == af_delete_NUM - 1
            logging.info('直埋段信息管理批量删除成功')
        except:
            logging.info('直埋段信息管理批量删除失败')
            l.getScreenShot('直埋段信息管理批量删除失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
