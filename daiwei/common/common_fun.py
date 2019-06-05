import time
import os
import csv
import logging
import win32api,win32gui,win32con
from daiwei.common.run_browser import launch_browser
from daiwei.common.baseView import BaseView


class Common(BaseView):

    def join_iframe(self):
        iframetest = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(iframetest)
        time.sleep(1)

    def quit_iframe(self):
        self.driver.switch_to.default_content()

    def win32_pick_slave(self, slavepath):
        # 获取到标题为打开的窗口
        procHandle = win32gui.FindWindow(None, u"打开")
        win32gui.SetForegroundWindow(procHandle)

        # 获取到类名为ComboBoxEx32的选择框
        edit = win32gui.FindWindowEx(procHandle, 0, "ComboBoxEx32", None)  # 获取句柄
        win32api.SendMessage(edit, win32con.WM_SETTEXT, 0, slavepath)  # 输入Excel模板路径
        openBt = win32gui.FindWindowEx(procHandle, 0, "Button", u'打开(&O)')  # 点击打开按钮

        # 进行鼠标的点击
        win32api.PostMessage(openBt, win32con.WM_LBUTTONDOWN, 0, 0)
        win32api.PostMessage(openBt, win32con.WM_LBUTTONUP, 0, 0)

    def gettime(self):
        self.now = time.strftime("%Y-%m-%d %H-%M-%S")
        return self.now

    def getScreenShot(self, module):
        time = self.gettime()
        # image_file = E:/python_project/daiwei
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/warehouse/screenshots/%s_%s.png' % (module, time)
        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self, csv_file, line):
        '''
        获取csv文件制定行的数据
        param csv_file：csv文件路径
        param line：数据行数
        return：
        '''
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    driver = launch_browser()
