from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import re

# 运维管理 - 标石录入 - 新增 - 删除

class BslrTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH, '//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    bslr = (By.XPATH, '//*[@id="tt1"]//*[text()="标石录入"]')  # 标石录入
    addBtn = (By.XPATH, '/html/body/div[1]/div[2]/div/a[1]')  # 新增
    bs_name = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[1]/td[2]/span[1]/input')  # 标石名称
    bs_text = '测试111'
    ba_type = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[3]/td[2]/span[1]')  # 标石类型
    ba_type_select = (By.XPATH, '/html/body/div[11]/div/div')  # 直埋标石
    province = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[5]/td[2]/span[1]')  # 所属省份
    province_select = (By.XPATH, '/html/body/div[10]/div/div')  # 北京市
    city = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[7]/td[2]/span[1]')  # 所属市
    city_select = (By.XPATH, '/html/body/div[15]/div/div')  # 北京市
    county = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[9]/td[2]/span')  # 区/县
    county_select = (By.XPATH, '/html/body/div[14]/div/div')  # 东城区
    longitude = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[11]/td[2]/span[1]/input')  # 经度
    longitude_num = '111'
    latitude = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[13]/td[2]/span[1]/input')  # 纬度
    latitude_num = '30'
    place_describe = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[15]/td[2]/span/input')  # 位置描述
    place_text = '东城区'
    property_nature = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[17]/td[2]/span[1]')  # 产权性质
    property_nature_select = (By.XPATH, '/html/body/div[12]/div/div')  # 自建
    maintain = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[19]/td[2]/span[1]')  # 维护方式
    maintain_select = (By.XPATH, '/html/body/div[13]/div/div')  # 综合代维
    cable_depth = (By.XPATH, '//*[@id="subjectorgForm"]/table/tbody/tr[21]/td[2]/span[1]/input')  # 光缆埋深
    cable_depth_num = '11'
    pick_slave = (By.XPATH, '//input[@id="picturepath"]')  # 选择文件
    slavepath = r'D:\1.jpg'  # 文件全路径
    submitBtn = (By.XPATH, '//*[@id="dd"]/div/div/a[1]/span/span')  # 提交
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/ul[2]/li[3]/a[2]')  # 重置
    bs_name_input = (By.XPATH, '//*[@id="searchBox"]/ul[1]/li[6]/span/input')  # 标石名称输入框
    searchBtn = (By.XPATH, '//*[@id="searchBox"]/ul[2]/li[3]/a[1]')  # 查询
    first_bs_name = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[2]/div/span')  # 第一条标石名称

    pageNum = (By.XPATH, '//*[@id="tt"]/div[1]/div/div[2]/div[1]')  # 右下角数据统计
    dele_firstBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[16]/div/a[2]')  # 第一条数据的删除按钮
    dele_certainBtn = (By.XPATH, '//*[text()="确定"]')  # 删除的确定

    first_sele = (By.XPATH, '//*[@id="datagrid-row-r1-2-9"]/td[1]/div/input')  # 勾选第10条数据
    batch_dele = (By.XPATH, '/html/body/div[1]/div[2]/div/a[6]')  # 批量删除
    batch_dele_certainBtn = (By.XPATH, '/html/body/div[25]/div[3]/a/span/span')  # 批量删除的确定



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
        self.driver.find_element(*self.bslr).click()
        l.join_iframe()
        time.sleep(3)

        # 新增
        self.driver.find_element(*self.addBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.bs_name).send_keys(*self.bs_text)
        self.driver.find_element(*self.ba_type).click()
        self.driver.find_element(*self.ba_type_select).click()
        self.driver.find_element(*self.province).click()
        self.driver.find_element(*self.province_select).click()
        self.driver.find_element(*self.city).click()
        self.driver.find_element(*self.city_select).click()
        self.driver.find_element(*self.county).click()
        self.driver.find_element(*self.county_select).click()
        self.driver.find_element(*self.longitude).send_keys(*self.longitude_num)
        self.driver.find_element(*self.latitude).send_keys(*self.latitude_num)
        self.driver.find_element(*self.place_describe).send_keys(*self.place_text)
        self.driver.find_element(*self.property_nature).click()
        self.driver.find_element(*self.property_nature_select).click()
        self.driver.find_element(*self.maintain).click()
        self.driver.find_element(*self.maintain_select).click()
        self.driver.find_element(*self.cable_depth).send_keys(*self.cable_depth_num)
        self.driver.find_element(*self.pick_slave).send_keys(*self.slavepath)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        be_PageNum = self.driver.find_element(*self.pageNum).text
        be_nums = re.findall(r'\d+\.?', be_PageNum)
        be_num = be_nums[2]
        be_NUM = int(be_num)
        logging.info('删除前共有数据%s条' % be_NUM)
        time.sleep(1)
        self.driver.find_element(*self.bs_name_input).send_keys(*self.bs_text)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(1)
        first_bs_text = self.driver.find_element(*self.first_bs_name).text
        try:
            assert self.bs_text == first_bs_text
            logging.info('标石录入新增成功')
        except:
            logging.info('标石录入新增失败')
            l.getScreenShot('标石录入新增失败')
        time.sleep(1)

    # 删除
        self.driver.find_element(*self.dele_firstBtn).click()
        time.sleep(0.5)
        self.driver.find_element(*self.dele_certainBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        af_PageNum = self.driver.find_element(*self.pageNum).text
        af_nums = re.findall(r'\d+\.?', af_PageNum)
        af_num = af_nums[2]
        af_NUM = int(af_num)
        logging.info('删除后共有数据%s条' % af_NUM)
        time.sleep(1)
        try:
            assert af_NUM == be_NUM - 1
            logging.info('标石录入删除成功')
        except:
            logging.info('标石录入删除失败')
            l.getScreenShot('标石录入删除失败')
        time.sleep(1)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)

    # 批量删除
        be_PageNum = self.driver.find_element(*self.pageNum).text
        be_nums = re.findall(r'\d+\.?', be_PageNum)
        be_num = be_nums[2]
        be_NUM = int(be_num)
        logging.info('批量删除前共有数据%s条' % be_NUM)
        time.sleep(1)
        self.driver.find_element(*self.first_sele).click()
        self.driver.find_element(*self.batch_dele).click()
        time.sleep(1)
        self.driver.find_element(*self.batch_dele_certainBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        af_PageNum = self.driver.find_element(*self.pageNum).text
        af_nums = re.findall(r'\d+\.?', af_PageNum)
        af_num = af_nums[2]
        af_NUM = int(af_num)
        logging.info('批量删除后共有数据%s条' % af_NUM)
        time.sleep(1)
        try:
            assert af_NUM == be_NUM - 1
            logging.info('标石录入批量删除成功')
        except:
            logging.info('标石录入批量删除失败')
            l.getScreenShot('标石录入批量删除失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
