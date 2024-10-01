from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from common.tools import get_project_path, sep

import warnings
from urllib3.exceptions import NotOpenSSLWarning
# Suppress the NotOpenSSLWarning
warnings.simplefilter("ignore", NotOpenSSLWarning)


#('/Users/hans/Desktop/code/python/automation/imooc_pytest/trading_system_test/driver_files/chromedriver')
chrome_service = Service(get_project_path()+sep(["driver_files", "chromedriver"],
                                                add_sep_before=True))

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--window-size=1200,800")
# disable enable-automation
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# ignore https certificate -errors
chrome_options.add_argument("--ignore-certificate-errors")
# ignore localhost TLS/SSL
chrome_options.add_argument("--allow-insecure-localhost")
# private mode
chrome_options.add_argument("--incognito")
# no application
#chrome_options.add_argument("--headless")
#
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


# 初始化 WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 打开百度网站
driver.get("http://www.tcpjwtester.top")

# 等待 10 秒
sleep(10)

# 关闭浏览器
driver.quit()

# if __name__ == '__main__':
#     pass