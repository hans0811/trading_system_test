from time import sleep

import allure

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage


class TestLogin:
    def test_login(self, driver):
        # driver = DriverConfig().driver_config()
        with allure.step("Login in"):
            LoginPage().login(driver, "test001")
            sleep(3)

        with allure.step("click left bar"):
            pass
        # driver.quit()

    # def test_login_negative(self):
    #     driver = DriverConfig().driver_config()
    #     driver.get("http://www.tcpjwtester.top")
    #     sleep(3)
    #     LoginPage().login_input_value(driver, '用户名', 'User')
    #     sleep(1)
    #     LoginPage().login_input_value(driver, '密码', '1234567')
    #     sleep(1)
    #     LoginPage().click_login(driver, '登录')
    #     sleep(3)
    #     driver.quit()
