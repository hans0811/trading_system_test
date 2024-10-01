from time import sleep

import allure

from base.report_add_img import add_img_2_report
from config.driver_config import DriverConfig
from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage


class TestWindowHandle:

    @allure.description("Window link")
    @allure.epic("Window epic")
    @allure.feature("Window feature")
    @allure.story("Window story")
    @allure.tag("Window tag")
    def test_switch_window_handles(self, driver):
        with allure.step("Login in"):
            #driver = DriverConfig().driver_config()
            LoginPage().login(driver, "test001")
            sleep(3)
            add_img_2_report(driver, "Login")

        with allure.step("click external link"):
            LeftMenuPage().click_level_one_menu(driver, "外链")
            sleep(1)
            add_img_2_report(driver, "external link")

        with allure.step("assert Title"):
            title = ExternalLinkPage().goto_imooc(driver)
            print("title:", title)
            assert title == "慕课网-程序员的梦工厂"
           # driver.quit()
