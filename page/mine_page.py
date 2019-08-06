# coding=utf-8
from util.get_by_local import GetByLocal


class MinePage:
    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver, "mine_element")

    def get_login_entrance(self):
        return self.get_by_local.get_element("login_entrance")

    def get_tab_mine(self):
        return self.get_by_local.get_element("tab_mine")

    def get_mine_req_entrance(self):
        return self.get_by_local.get_element("mine_req_entrance")

    def get_back_button(self):
        return self.get_by_local.get_element("back_button", "ALL")