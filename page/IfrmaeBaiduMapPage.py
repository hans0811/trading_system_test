from selenium.webdriver.common.by import By

from base.IframeBaiduMapBase import IframeBaiduMapBase
from base.ObjectMap import ObjectMap


class IframeBaiduMapPage(IframeBaiduMapBase, ObjectMap):

    def get_baidu_map_search_button(self, driver):
        button_xpath = self.search_button()
        return self.element_get(driver, By.Xpath, button_xpath)


    def switch_2_baidu_map_iframe(self, driver):
        iframe_xpath = self.baidu_map_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def iframe_out(self, driver):
        return self.switch_from_iframe_to_content(driver)