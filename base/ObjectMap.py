import time
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, \
    NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

from common.find_img import FindImg
from common.tools import get_project_path, sep
from common.yaml_config import GetConf


class ObjectMap:
    # Get Index
    url = GetConf().get_url()

    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_be_visible=False):
        start_ms = time.time() * 1000
        stop_ms = start_ms + (timeout * 1000)

        for x in range(int(timeout * 1000)):
            # todo find elememt
            try:
                element = driver.find_element(by=locate_type, value=locator_expression)

                if not must_be_visible:
                    return element
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break
                pass
            time.sleep(0.1)

        raise ElementNotVisibleException("Type:" + locate_type + " expression: " + locator_expression)

    def wait_for_ready_state_complete(self, driver, timeout=30):

        # Start time
        start_ms = time.time() * 1000
        # End time
        stop_ms = start_ms + (timeout * 1000)

        for x in range(int(timeout * 10)):
            try:
                ready_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                # Execute Javascript failed
                time.sleep(0.03)
                return True

            if ready_state == "complete":
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                # timeout
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        raise Exception("Page timeout after %s" % timeout)

    def element_disappear(self, driver, locate_type, locator_expression, timeout=30):
        if locate_type:
            start_ms = time.time() * 1000
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception("Element not show:" + locate_type + "\n" + locator_expression)
        else:
            pass

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        if locate_type:
            start_ms = time.time() * 1000
            stop_ms = start_ms + (timeout * 1000)

            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.1)
                    pass
            raise ElementNotVisibleException("Element not show: " + locate_type + "/n" + locator_expression)
        else:
            pass

    def element_to_url(
            self,
            driver,
            url,
            locate_type_disappear=None,
            locator_expression_disappear=None,
            locate_type_appear=None,
            locator_expression_appear=None
    ) -> bool:
        try:
            driver.get(self.url + url)

            # Wait Element loading
            self.wait_for_ready_state_complete(driver)
            # redirect wait for element disappear
            self.element_disappear(driver,
                                   locate_type_disappear,
                                   locator_expression_disappear
                                   )
            # Redirect wait for element show
            self.element_appear(
                driver,
                locate_type_appear,
                locator_expression_appear
            )
        except Exception as e:
            print("Redirect error, $s" % e)
            return False

        return True

    def element_is_display(self, driver, locate_type, locator_expression):
        try:
            driver.find_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException:
            return False

    def element_is_display(self, driver, locate_type, locator_expression):
        """
        元素是否显示
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        try:
            driver.find_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False

    def element_fill_value(self, driver, locate_type, locator_expression, fill_value, timeout=30):
        """
        元素填值
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param fill_value: 填入的值
        :param timeout: 超时时间
        :return:
        """
        # 元素必须先出现
        element = self.element_appear(
            driver,
            locate_type=locate_type,
            locator_expression=locator_expression,
            timeout=timeout
        )
        try:
            # 先清除元素中的原有值
            element.clear()
        except StaleElementReferenceException:  # 页面元素没有刷新出来，就对元素进行捕获，从而引发了这个异常
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(
                driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout
            )
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass
        # 填入的值转成字符串
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)
        try:
            # 填入的值不是以\n结尾
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type=locate_type, locator_expression=locator_expression)
            element.clear()
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except Exception:
            raise Exception("元素填值失败")

        return True

    def element_click(
            self,
            driver,
            locate_type,
            locator_expression,
            locate_type_disappear=None,
            locator_expression_disappear=None,
            locate_type_appear=None,
            locator_expression_appear=None,
            timeout=30
    ):
        element = self.element_appear(
            driver=driver,
            locate_type=locate_type,
            locator_expression=locator_expression,
            timeout=timeout
        )

        try:
            element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(
                dirver=driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout
            )
            element.click()
        except Exception as e:
            print("Element cannot click", e)
            return False

        try:

            self.element_appear(
                driver,
                locate_type_appear,
                locator_expression_appear
            )

            self.element_disappear(
                driver,
                locate_type_disappear,
                locator_expression_disappear
            )
        except Exception as e:
            print("Wait element", e)
            return False

        return True

    def upload(self, driver, locate_type, locator_expression, file_path):
        element = self.element_get(driver, locate_type, locator_expression)
        return element.send_keys(file_path)

    def switch_window_2_latest_handle(self, driver):
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

    def switch_into_iframe(self,
                           driver,
                           locate_iframe_type,
                           locate_iframe_expression):
        iframe = self.element_get(driver, locate_iframe_type, locate_iframe_expression)
        driver.switch_to.frame(iframe)

    def switch_from_iframe_to_content(self, driver):
        driver.switch_to.parent_frame()

    def find_img_in_source(self, driver, img_name) -> float:

        # save source
        source_img_path = get_project_path() + sep(["img", "source_img", img_name], add_sep_before=True)
        print("source_img_path:", source_img_path)
        # save target
        search_img_path = get_project_path() + sep(["img", "assert_img", img_name], add_sep_before=True)
        print("search_img_path:", search_img_path)
        # 截图并保存图片
        driver.get_screenshot_as_file(source_img_path)
        time.sleep(3)
        # add_img_path_2_report(source_img_path, "原图")
        # add_img_path_2_report(search_img_path, "需要查找的图")
        # 在原图中查找是否有指定的图片，返回信心值
        confidence = FindImg().get_confidence(source_img_path, search_img_path)
        return confidence


if __name__ == '__main__':
    objectMap = ObjectMap()

    print(objectMap.element_get())
