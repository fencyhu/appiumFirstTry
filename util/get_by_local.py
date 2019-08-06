# coding=utf-8
from appium.webdriver.webdriver import WebDriver

from util.read_ini import ReadIni


class GetByLocal:

    def __init__(self, driver, section=None):
        self.driver = driver
        self.section = section

    def get_element(self, key, section=None):
        read_ini = ReadIni()
        if section is None:
            section = self.section
        local = read_ini.get_value(key, section)
        print local
        if local is None:
            return None
        by = local.split(">")[0]
        local_by = local.split(">")[1]
        try:
            if by == "id":
                return self.driver.find_element_by_id(local_by)
            elif by == "classname":
                return self.driver.find_element_by_class_name(local_by)
            else:
                return self.driver.find_element_by_xpath(local_by)
        except:
            self.driver.save_screenshot("../jpg/test.png")
            return None

    def get_coordinate(self, key, section):
        read_ini = ReadIni()
        local = read_ini.get_value(key, section)
        if local is None:
            return None
        local_by = local.split(">")[1]
        size = self.driver.get_window_size()
        x = int(float(local_by.split(",")[0]) * size['width'])
        y = int(float(local_by.split(",")[1]) * size['height'])
        return x, y




