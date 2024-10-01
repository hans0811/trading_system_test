from time import sleep

from page.LoginPage import LoginPage


class TestLoginAssert:
    def test_login_assert(self, driver):
        LoginPage().login(driver, "test001")
        sleep(3)
        assert LoginPage().login_assert(driver, "head_img.jpg") > 0.9
