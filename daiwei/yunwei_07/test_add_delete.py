from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import re

# 运维管理 - 电杆录入 - 新增 - 删除

class DglrTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH,'//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH,'//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    dglr = (By.XPATH,'//*[@id="tt1"]//*[text()="电杆录入"]')  # 电杆录入
    addBtn = (By.XPATH,'/html/body/div[1]/div[2]/div/a[1]')  # 新增
    pole_name_input = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[1]/td[2]/span[1]/input')  # 电杆名称
    pole_name_text = '测试111'  # 电杆名称
    pull_line_input = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[1]/td[4]/span[1]/input')  # 拉线条数
    pull_line_num = '11'  # 拉线条数
    pole_type = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[3]/td[2]/span[1]')  # 电杆类型
    pole_type_select = (By.XPATH,'/html/body/div[11]/div/div[4]')  # 水泥杆
    pole_material = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[3]/td[4]/span[1]')  # 电杆材料
    pole_material_select = (By.XPATH,'/html/body/div[12]/div/div[2]')  # 水泥
    province = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[5]/td[2]/span[1]')  # 所属省份
    province_select = (By.XPATH,'/html/body/div[10]/div/div')  # 北京市
    city = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[5]/td[4]/span[1]')  # 所属市
    city_select = (By.XPATH,'/html/body/div[17]/div/div')  # 北京市
    pole_height = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[7]/td[4]/span[1]/input')  # 电杆高度
    pole_height_num = '11'  # 电杆高度
    property_unit = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[9]/td[2]/span[1]')  # 产权单位
    property_select = (By.XPATH,'/html/body/div[13]/div/div[3]')  # 电信
    province_nature = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[9]/td[4]/span[1]')  # 产权性质
    nature_select = (By.XPATH,'/html/body/div[14]/div/div')  # 自建
    longitude_input = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[11]/td[2]/span[1]/input')  # 经度
    longitude_text = '150'  # 经度
    latitude_input = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[11]/td[4]/span[1]/input')  # 纬度
    latitude_text = '50'  # 纬度
    uphold_method = (By.XPATH,'//*[@id="subjectorgForm"]/table/tbody/tr[13]/td[4]/span[1]')  # 维护方式
    uphold_select = (By.XPATH,'/html/body/div[15]/div/div')  # 综合代维
    select_file = (By.XPATH,'//*[@id="picturepath"]')  # 选择文件
    slavepath = r'D:\1.jpg'  # 文件全路径
    submitBtn = (By.XPATH,'//*[@id="dd"]/div/div/a[1]/span/span')  # 提交
    resetBtn=(By.XPATH,'//*[@id="searchBox"]/ul[2]/li[4]/a[2]')  # 重置
    first_pole_name = (By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[2]/div/span')  # 新增后第一条数据的电杆名称
    pageNum = (By.XPATH, '//*[@id="tt"]/div[1]/div/div[2]/div[1]')  # 右下角数据统计
    dele_firstBtn=(By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[19]/div/a[2]/img')  # 第一条数据的删除按钮
    dele_certainBtn=(By.XPATH,'/html/body/div[22]/div[3]/a[1]/span/span')  # 删除的确定



    first_sele=(By.XPATH,'//*[@id="datagrid-row-r1-2-9"]/td[1]/div/input')  # 勾选第10条数据
    batch_dele=(By.XPATH,'/html/body/div[1]/div[2]/div/a[6]')  # 批量删除
    batch_dele_certainBtn=(By.XPATH,'/html/body/div[22]/div[3]/a[1]/span/span')  # 批量删除的确定


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
        self.driver.find_element(*self.dglr).click()
        l.join_iframe()
        time.sleep(3)

# 新增
        self.driver.find_element(*self.addBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.pole_name_input).send_keys(*self.pole_name_text)
        self.driver.find_element(*self.pull_line_input).send_keys(*self.pull_line_num)
        self.driver.find_element(*self.pole_type).click()
        self.driver.find_element(*self.pole_type_select).click()
        self.driver.find_element(*self.pole_material).click()
        self.driver.find_element(*self.pole_material_select).click()
        self.driver.find_element(*self.province).click()
        self.driver.find_element(*self.province_select).click()
        self.driver.find_element(*self.city).click()
        self.driver.find_element(*self.city_select).click()
        self.driver.find_element(*self.pole_height).send_keys(*self.pole_height_num)
        self.driver.find_element(*self.property_unit).click()
        self.driver.find_element(*self.property_select).click()
        self.driver.find_element(*self.province_nature).click()
        self.driver.find_element(*self.nature_select).click()
        self.driver.find_element(*self.longitude_input).send_keys(*self.longitude_text)
        self.driver.find_element(*self.latitude_input).send_keys(*self.latitude_text)
        self.driver.find_element(*self.uphold_method).click()
        self.driver.find_element(*self.uphold_select).click()
        self.driver.find_element(*self.select_file).click()
        time.sleep(2)
        l.win32_pick_slave(self.slavepath)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(3)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(2)
        first_pole_text = self.driver.find_element(*self.first_pole_name).text
        try:
            assert self.pole_name_text == first_pole_text
            logging.info('电杆录入新增成功')
        except:
            logging.info('电杆录入新增失败')
            l.getScreenShot('电杆录入新增失败')

# 删除
        be_PageNum = self.driver.find_element(*self.pageNum).text
        be_nums = re.findall(r'\d+\.?', be_PageNum)
        be_num = be_nums[2]
        be_NUM = int(be_num)
        logging.info('删除前共有数据%s条' % be_NUM)
        time.sleep(1)
        self.driver.find_element(*self.dele_firstBtn).click()
        self.driver.find_element(*self.dele_certainBtn).click()
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
            logging.info('电杆录入删除成功')
        except:
            logging.info('电杆录入删除失败')
            l.getScreenShot('电杆录入删除失败')
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
            logging.info('电杆录入批量删除成功')
        except:
            logging.info('电杆录入批量删除失败')
            l.getScreenShot('电杆录入批量删除失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
