# coding=utf-8
from appium import webdriver
import time
import datetime
from util.write_user_command import WriteUserCmd


class BaseDriver:

    def __init__(self):
        self.write_user_cmd = WriteUserCmd()

    def ios_driver(self, i):
        key = "user_info_"+str(i)
        device = self.write_user_cmd.get_value(key, "deviceId")
        port = self.write_user_cmd.get_value(key, "port")
        capability = {
            "platformName": "iOS",
            "platformVersion": "12.3.1",
            "deviceName": "Fency's iPhone",
            "automationName": "XCUITest",
            "bundleId": "com.daojia.jz.app",
            'newCommandTimeout': "200",
            "udid": device,
            "clearSystemFiles": "true"
        }
        url = "http://127.0.0.1:"+port+"/wd/hub"
        print datetime.datetime.now(), url, capability
        driver = webdriver.Remote(url, capability)

        time.sleep(5)
        # driver.switch_to.alert.accept()

        return driver
