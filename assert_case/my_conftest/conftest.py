import pytest

from config.driver_config import DriverConfig


@pytest.fixture()
def driver():
    print("Open Browser")
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()
    print("Quit Browser")