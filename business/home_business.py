# coding=utf-8

from handle.home_handle import HomeHandle


class HomeBusiness:

    def __init__(self, driver):
        self.home_handle = HomeHandle(driver)

    def city_change_accept(self):
        if self.home_handle.get_city_change_alert():
            self.home_handle.accept_city_change()
        else:
            return False

    def city_change_cancel(self):
        if self.home_handle.get_city_change_alert():
            self.home_handle.cancel_city_change()
        else:
            return False




