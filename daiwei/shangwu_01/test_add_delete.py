from daiwei.common.baseView import BaseView
from daiwei.common.myunit import StartEnd
from daiwei.common.loginView import LoginView
from daiwei.common.quitView import QuitView
from selenium.webdriver.common.by import By
import unittest
import time
import logging
import re

# 商务管理 - 标书费 - 新增 - 删除

class BsfTest(StartEnd, BaseView):

    swglBtn=(By.XPATH,'//*[@id="css3menu"]//*[text()="商务管理"]')  # 商务管理
    bsfBtn=(By.XPATH,'//*[@id="tt1"]//*[text()="标书费"]')  # 标书费
    addBtn=(By.XPATH,'//*[@id="tool"]/form/div[2]/div/a')  # 新增
    xmname=(By.XPATH,'//*[@id="_easyui_textbox_input4"]')  # 项目名称
    text_xmmc = '测试777'  # 项目名称
    skr=(By.XPATH,'//*[@id="_easyui_textbox_input5"]')  # 收款人
    text_skr = '测试888'  # 收款人
    skje=(By.XPATH,'//*[@id="_easyui_textbox_input6"]')  # 金额
    text_je = '888'  # 金额
    kbsj=(By.XPATH,'//*[@id="_easyui_textbox_input11"]')  # 开标时间
    today=(By.XPATH,'/html/body/div[6]/div/div[2]/table/tbody/tr/td[1]/a')  # 选择开标时间
    phone=(By.XPATH,'//*[@id="_easyui_textbox_input7"]')  # 联系电话
    text_ph = '15866663333'  # 联系电话
    OANUM=(By.XPATH,'//*[@id="_easyui_textbox_input8"]')  # OA号
    text_OA = 'OA3333'  # OA号
    invo=(By.XPATH,'//*[@id="myFormId"]/table[1]/tbody/tr[7]/td[2]/span/span/a')  # 发票是否取回
    invo_sele=(By.XPATH,'//*[@id="_easyui_combobox_i1_1"]')  # 发票是否取回-选择
    add_sub=(By.XPATH,'//*[@id="myFormId"]/table[2]/tbody/tr/td/a[1]')  # 新增标书费信息-提交
    first_xmmc=(By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[1]/div/span')  # 新增数据的项目名称

    search_xmmc=(By.XPATH,'//*[@id="searchBox"]/div/div/span/input')  # 搜索框-项目名称
    searchBtn=(By.XPATH,'//*[@id="searchBox"]/div[1]/div[4]/a[1]')  # 搜索

    dele_firstBtn=(By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[9]/div/a[2]')  # 第一条数据的删除按钮
    dele_certainBtn=(By.XPATH,'/html/body/div[7]/div[3]/a[1]/span/span')  # 删除的确定
    resetBtn=(By.XPATH,'//*[@id="searchBox"]/div[1]/div[4]/a[2]')  # 重置

    pageNum=(By.XPATH,'//*[@id="tt"]/div[1]/div/div[3]/div[1]')  # 右下角数据统计

    first_sele=(By.XPATH,'//*[@id="datagrid-row-r1-1-0"]/td[2]/div/input')  # 勾选第一条数据
    batch_dele=(By.XPATH,'//*[@id="searchBox"]/div[2]/div/a[2]')  # 批量删除
    batch_dele_certainBtn=(By.XPATH,'/html/body/div[7]/div[3]/a[1]/span/span')  # 批量删除的确定


    def test_login_zhaobingcheng(self):
        logging.info('=========test_login_zhaobingcheng============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        time.sleep(2)

# 新增
        self.driver.find_element(*self.swglBtn).click()
        self.driver.find_element(*self.bsfBtn).click()
        l.join_iframe()
        time.sleep(1)
        self.driver.find_element(*self.addBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.xmname).send_keys(*self.text_xmmc)
        self.driver.find_element(*self.skr).send_keys(*self.text_skr)
        self.driver.find_element(*self.skje).send_keys(*self.text_je)
        self.driver.find_element(*self.kbsj).click()
        self.driver.find_element(*self.today).click()
        self.driver.find_element(*self.phone).send_keys(*self.text_ph)
        self.driver.find_element(*self.OANUM).send_keys(*self.text_OA)
        self.driver.find_element(*self.invo).click()
        self.driver.find_element(*self.invo_sele).click()
        self.driver.find_element(*self.add_sub).click()
        time.sleep(2)
        First_xmmc=self.driver.find_element(*self.first_xmmc).text
        try:
            assert self.text_xmmc == First_xmmc
            logging.info('===标书费新增成功===')
        except:
            logging.info('===标书费新增失败===')
            l.getScreenShot('标书费新增失败')

# 搜索
        self.driver.find_element(*self.search_xmmc).send_keys(*self.text_xmmc)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(2)
        try:
            assert self.text_xmmc == First_xmmc
            logging.info('===标书费搜索成功===')
        except:
            logging.info('===标书费搜索失败===')
            l.getScreenShot('标书费搜索失败')

# 删除
        self.driver.find_element(*self.dele_firstBtn).click()
        self.driver.find_element(*self.dele_certainBtn).click()
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(2)
        First_xmmc_1=self.driver.find_element(*self.first_xmmc).text
        time.sleep(1)
        try:
            assert self.text_xmmc == First_xmmc_1
            logging.info('===标书费删除失败===')
            l.getScreenShot('标书费删除失败')
        except:
            logging.info('===标书费删除成功===')

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
        af_PageNum = self.driver.find_element(*self.pageNum).text
        af_nums = re.findall(r'\d+\.?', af_PageNum)
        af_num = af_nums[2]
        af_NUM = int(af_num)
        logging.info('批量删除后共有数据%s条' % af_NUM)
        time.sleep(1)
        try:
            assert af_NUM == be_NUM - 1
            logging.info('===标书费批量删除成功===')
        except:
            logging.info('===标书费批量删除失败===')
            l.getScreenShot('标书费批量删除失败')
        self.driver.find_element(*self.resetBtn).click()
        time.sleep(1)
        l.quit_iframe()
        k = QuitView(self.driver)
        k.quit_action()


if __name__ == '__main__':
    unittest.main()
