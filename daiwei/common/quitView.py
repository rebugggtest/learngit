import logging
import time
from daiwei.common.common_fun import Common
from daiwei.common.run_browser import launch_browser
from selenium.webdriver.common.by import By


class QuitView(Common):

    zxBtn = (By.XPATH, '//*[@id="north"]/div[1]/div[2]/ul/li[2]/a')
    qrBtn = (By.XPATH, '/html/body/div[9]/div[3]/a[1]/span/span')

    def quit_action(self):

        logging.info('============quit============')
        self.driver.find_element(*self.zxBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.qrBtn).click()


if __name__ == '__main__':
    driver = launch_browser()
