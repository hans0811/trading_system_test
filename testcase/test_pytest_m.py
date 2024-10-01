from time import sleep

import pytest

from config.driver_config import DriverConfig


class TestPytestMClass:

    @pytest.fixture(scope="class")
    def scope_class(self):
        print("Class Lever: Only execute once")

    @pytest.fixture(scope="function")
    def driver(self):
        get_driver = DriverConfig().driver_config()
        return get_driver

    @pytest.mark.test001
    def test_open_bing(self, driver, scope_class):
        # driver = DriverConfig().driver_config()
        driver.get("https://google.com")
        sleep(3)
        driver.quit()

    @pytest.mark.test002
    def test_open_test002(self, driver, scope_class):
        print("test_open_being")
        # driver = DriverConfig().driver_config()
        driver.get("https://www.bing.com/")
        sleep(3)
        driver.quit()

    @pytest.mark.test003
    def test_open_test003(self, driver, scope_class):
        # driver = DriverConfig().driver_config()
        driver.get("https://www.yahoo.com/")
        sleep(3)
        driver.quit()
