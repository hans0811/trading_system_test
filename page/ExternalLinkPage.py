from base.ObjectMap import ObjectMap


class ExternalLinkPage(ObjectMap):

    def goto_imooc(self, driver):
        self.switch_window_2_latest_handle(driver)
        return driver.title
