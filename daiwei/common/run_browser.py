import logging.config
import os
import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler
from selenium import webdriver

CON_LOG = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
CON_LOG = CON_LOG + r'\daiwei\config\log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def launch_browser():

    logging.info('start run browser...')
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    base_url = "http://192.168.0.8:8084/YDDWXT/login.jsp"
    driver.maximize_window()
    driver.get(base_url)
    return driver


if __name__ == '__main__':
    launch_browser()
