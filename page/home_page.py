# coding=utf-8
from util.get_by_local import GetByLocal


class HomePage:
    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)

    def get_cityChangeArlert_ele(self):
        return self.get_by_local.get_element("location_alert", "home_element")

    def get_cityChangeAcceptButton_loc(self):
        return self.get_by_local.get_coordinate("location_alert_accept", "home_element")

    def get_cityChangeCancelButton_loc(self):
        return self.get_by_local.get_coordinate("location_alert_cancel", "home_element")

    def get_tab_home(self):
        return self.get_by_local.get_element("tab_home", "home_element")
