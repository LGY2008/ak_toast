import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver: object) -> object:
        self.driver = driver

    # 查找元素封装
    def find_element(self, loc, timeout=5, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    # 查找所有一组元素封装
    def find_elements(self, loc, timeout=5, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    # 单个元素封装
    def find_element_xpath_click(self, value, timeout=5, poll=0.5):
        WebDriverWait(self.driver, timeout, poll).until(
            lambda x: x.find_element_by_xpath("//*[contains(@text,'" + value + "')]")).click()

    # 点击元素 封装
    def base_click_element(self, loc):
        self.find_element(loc).click()

    # 点击单个元素
    def base_click(self, elements, num=0):
        """
        :param elements: 传入元素列表
        :param num:指定下标，默认为0
        :return:
        """
        elements[num].click()

    # 输入文本 封装
    def base_input_text(self, loc, value):
        el = self.find_element(loc)
        el.clear()
        el.send_keys(value)

    # 获取文本
    def base_get_text(self, loc):
        return self.find_element(loc).text

    # 滑动
    def base_drag_and_drop(self, el1, el2):
        self.driver.drag_and_drop(el1, el2)

    # 获取 toast
    def base_get_toast(self, loc):
        return self.find_element(loc, poll=0.1)

    # 截屏
    def base_get_screen_shot(self):
        time_stamp = str(int(time.time()))
        file_path = os.getcwd() + os.sep + "Image" + os.sep + time_stamp + ".png"
        self.driver.get_screenshot_as_file(file_path)

    # 获取toast
    def base_get_toast_info(self, message):
        message = "//*[contains(@text,'" + message + "')]"
        return self.base_get_toast((By.XPATH, message)).text

    # 获取元素属性值
    def base_get_attribute_value(self, loc, attribute):
        return self.find_element(loc).get_attribute(attribute)
