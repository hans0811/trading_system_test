from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import chromedriver_autoinstaller

class DriverConfig:
    def driver_config(self):
        """
        浏览器驱动
        :return:
        """
        # Automatically installs the correct version of chromedriver
        chromedriver_autoinstaller.install()

        options = webdriver.ChromeOptions()
        # 设置窗口大小，设置为1920*1080
        options.add_argument("window-size=1920,1080")
        # 去除"chrome正受到自动测试软件的控制"的提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决selenium无法访问https的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略localhost上的TLS/SSL错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        options.add_argument("--incognito")
        # 解决卡顿
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Initialize ChromeDriver with the correct version
        driver = webdriver.Chrome(
            service=webdriver.chrome.service.Service(ChromeDriverManager(
                url="https://registry.npmmirror.com/-/binary/chromedriver",
                latest_release_url="https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE"
            ).install()),
            options=options
        )

        # 删除所有cookies
        driver.delete_all_cookies()

        return driver