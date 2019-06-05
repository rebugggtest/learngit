from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import re

# 运维管理 - 人手井录入 - 新增 - 删除

class RsjlrTest(StartEnd, BaseView):

    ywglBtn = (By.XPATH, '//*[@id="css3menu"]//*[text()="运维管理"]')  # 运维管理
    gxzygl = (By.XPATH, '//*[@id="tt1"]//*[text()="管线资源管理"]')  # 管线资源管理
    rsjlr = (By.XPATH, '//*[@id="tt1"]//*[text()="人手井录入"]')  # 人手井录入
    addBtn = (By.XPATH, '//*[@id="addId"]')  # 新增
    rsj_name_input = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[1]/td[2]/span[1]/input')  # 井名称
    rsj_name_text = '测试111'  # 井名称
    rsj_material = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[1]/td[4]/span')  # 人手井材质
    rsj_material_select = (By.XPATH, '/html/body/div[12]/div/div')  # 混凝土
    rsj_type = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[2]/td[2]/span')  # 人手井类型
    rsj_type_select = (By.XPATH, '/html/body/div[13]/div/div[2]')  # 手井
    rsj_model = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[2]/td[4]/span')  # 人手井型号
    rsj_model_select = (By.XPATH, '/html/body/div[14]/div/div[2]')  # 三通
    province = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[3]/td[2]/span[1]')  # 所属省份
    province_select = (By.XPATH, '/html/body/div[21]/div/div')  # 北京市
    city = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[3]/td[4]/span[1]')  # 所属市
    city_select = (By.XPATH, '/html/body/div[23]/div/div')  # 北京市
    county = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[4]/td[2]/span')  # 区/县
    county_select = (By.XPATH, '/html/body/div[22]/div/div')  # 东城区
    holes = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[4]/td[4]/span/input')  # 管孔数
    holes_num = '11'
    longitude = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[5]/td[2]/span/input')  # 经度
    longitude_num = '111'
    latitude = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[5]/td[4]/span/input')  # 纬度
    latitude_num = '30'
    manhole_shape = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[6]/td[2]/span/input')  # 井盖形状
    manhole_shape_text = '五角形'
    manhole_size = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[6]/td[4]/span/input')  # 井盖尺寸
    manhole_size_text = '5'
    manhole_material = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[7]/td[2]/span')  # 井盖材质
    manhole_material_select = (By.XPATH, '/html/body/div[15]/div/div[3]')  # 水泥
    dx_length = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[7]/td[4]/span/input')  # 东西长
    dx_length_text = '11'
    nb_length = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[8]/td[2]/span/input')  # 南北长
    nb_length_text = '11'
    well_deep = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[8]/td[4]/span/input')  # 井深
    well_deep_text = '12'
    well_high = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[9]/td[2]/span/input')  # 净井高
    well_high_text = '12'
    property_unit = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[9]/td[4]/span')  # 产权单位
    property_unit_select = (By.XPATH, '/html/body/div[16]/div/div[3]')  # 电信
    property_nature = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[10]/td[2]/span')  # 产权性质
    property_nature_select = (By.XPATH, '/html/body/div[17]/div/div[1]')  # 自建
    rode_name = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[10]/td[4]/span/input')  # 路段名称
    rode_name_text = '1to2'
    maintain = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[11]/td[2]/span')  # 维护方式
    maintain_select = (By.XPATH, '/html/body/div[18]/div/div')  # 综合代维
    lbj = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[11]/td[4]/span/input')  # 管道井路边距
    lbj_text = '11'
    lzj = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[12]/td[2]/span/input')  # 管道井路中距
    lzj_text = '11'
    manhole = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[12]/td[4]/span')  # 是否有井内盖
    manhole_select = (By.XPATH, '/html/body/div[19]/div/div[2]')  # 有
    worn = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[13]/td[2]/span')  # 是否破损
    worn_select = (By.XPATH, '/html/body/div[20]/div/div')  # 否
    manhole_num = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[13]/td[4]/span/input')  # 井盖数量
    manhole_num_text = '5'
    bottom_width = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[14]/td[2]/span/input')  # 井底宽
    bottom_width_text = '400'
    level_high = (By.XPATH, '//*[@id="myFormId"]/table[1]/tbody/tr[14]/td[4]/span/input')  # 水平高度
    level_high_text = '20'
    pick_slave = (By.XPATH, '//input[@id="picturepath"]')  # 选择文件
    slavepath = r'D:\1.jpg'  # 文件全路径
    submitBtn = (By.XPATH, '//*[@id="myFormId"]/div/a[1]/span/span')  # 提交
    resetBtn = (By.XPATH, '//*[@id="searchBox"]/div/div[9]/a[2]')  # 重置
    well_name_input = (By.XPATH, '//*[@id="searchBox"]/div/div[6]/span/input')  # 井名称输入框
    searchBtn = (By.XPATH, '//*[@id="searchBox"]/div/div[9]/a[1]')  # 查询
    first_well_name = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[2]/div/span')  # 第一条数据的井名称
    pageNum = (By.XPATH, '/html/body/div[1]/div/div[3]/div[1]')  # 右下角数据统计
    dele_firstBtn = (By.XPATH, '//*[@id="datagrid-row-r1-2-0"]/td[33]/div/a[2]')  # 第一条数据的删除按钮
    dele_certainBtn = (By.XPATH, '/html/body/div[24]/div[3]/a[1]/span/span')  # 删除的确定

    first_sele = (By.XPATH, '//*[@id="datagrid-row-r1-2-9"]/td[1]/div/input')  # 勾选第10条数据
    batch_dele = (By.XPATH, '//*[@id="tool"]/div/div/a[6]')  # 批量删除
    batch_dele_certainBtn = (By.XPATH, '/html/body/div[24]/div[3]/a/span/span')  # 批量删除的确定



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
        self.driver.find_element(*self.rsjlr).click()
        l.join_iframe()
        time.sleep(3)

        # 新增
        self.driver.find_element(*self.addBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.rsj_name_input).send_keys(self.rsj_name_text)
        self.driver.find_element(*self.rsj_material).click()
        self.driver.find_element(*self.rsj_material_select).click()
        self.driver.find_element(*self.rsj_type).click()
        self.driver.find_element(*self.rsj_type_select).click()
        self.driver.find_element(*self.rsj_model).click()
        self.driver.find_element(*self.rsj_model_select).click()
        self.driver.find_element(*self.province).click()
        self.driver.find_element(*self.province_select).click()
        self.driver.find_element(*self.city).click()
        self.driver.find_element(*self.city_select).click()
        self.driver.find_element(*self.county).click()
        self.driver.find_element(*self.county_select).click()
        self.driver.find_element(*self.holes).send_keys(*self.holes_num)
        self.driver.find_element(*self.longitude).send_keys(*self.longitude_num)
        self.driver.find_element(*self.latitude).send_keys(*self.latitude_num)
        self.driver.find_element(*self.manhole_shape).send_keys(*self.manhole_shape_text)
        self.driver.find_element(*self.manhole_size).send_keys(*self.manhole_size_text)
        self.driver.find_element(*self.manhole_material).click()
        self.driver.find_element(*self.manhole_material_select).click()
        self.driver.find_element(*self.dx_length).send_keys(*self.dx_length_text)
        self.driver.find_element(*self.nb_length).send_keys(*self.nb_length_text)
        self.driver.find_element(*self.well_deep).send_keys(*self.well_deep_text)
        self.driver.find_element(*self.well_high).send_keys(*self.well_high_text)
        self.driver.find_element(*self.property_unit).click()
        self.driver.find_element(*self.property_unit_select).click()
        self.driver.find_element(*self.property_nature).click()
        self.driver.find_element(*self.property_nature_select).click()
        self.driver.find_element(*self.rode_name).send_keys(*self.rode_name_text)
        self.driver.find_element(*self.maintain).click()
        self.driver.find_element(*self.maintain_select).click()
        self.driver.find_element(*self.lbj).send_keys(*self.lbj_text)
        self.driver.find_element(*self.lzj).send_keys(*self.lzj_text)
        self.driver.find_element(*self.manhole).click()
        self.driver.find_element(*self.manhole_select).click()
        self.driver.find_element(*self.worn).click()
        self.driver.find_element(*self.worn_select).click()
        self.driver.find_element(*self.manhole_num).send_keys(*self.manhole_num_text)
        self.driver.find_element(*self.bottom_width).send_keys(*self.bottom_width_text)
        self.driver.find_element(*self.level_high).send_keys(*self.level_high_text)
        self.driver.find_element(*self.pick_slave).send_keys(*self.slavepath)
        self.driver.find_element(*self.submitBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        be_PageNum = self.driver.find_element(*self.pageNum).text
        be_nums = re.findall(r'\d+\.?', be_PageNum)
        be_num = be_nums[2]
        be_NUM = int(be_num)
        logging.info('删除前共有数据%s条' % be_NUM)
        time.sleep(1)
        self.driver.find_element(*self.well_name_input).send_keys(*self.rsj_name_text)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(2)
        well_name_search = self.driver.find_element(*self.first_well_name).text
        try:
            assert self.rsj_name_text == well_name_search
            logging.info('人手井录入新增成功')
        except:
            logging.info('人手井录入新增失败')
            l.getScreenShot('人手井录入新增失败')

    # 删除
        self.driver.find_element(*self.dele_firstBtn).click()
        self.driver.find_element(*self.dele_certainBtn).click()
        time.sleep(1)
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
            logging.info('人手井录入删除成功')
        except:
            logging.info('人手井录入删除失败')
            l.getScreenShot('人手井录入删除失败')
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
            logging.info('人手井录入批量删除成功')
        except:
            logging.info('人手井录入批量删除失败')
            l.getScreenShot('人手井录入批量删除失败')

        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
