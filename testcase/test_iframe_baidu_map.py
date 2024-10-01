from time import sleep

from config.driver_config_raw import DriverConfig
from page.IfrmaeBaiduMapPage import IframeBaiduMapPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage


class TestIframeBaiduMap:

    def test_iframe_baidu_map(self, driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, "test001")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver,"iframe测试")
        sleep(1)
        IframeBaiduMapPage().switch_2_baidu_map_iframe(driver)
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        IframeBaiduMapPage().iframe_out(driver)
        LeftMenuPage().click_level_one_menu(driver, "首页")
        sleep(3)
        # driver.quit()
