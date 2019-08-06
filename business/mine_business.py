# coding=utf-8

from handle.mine_handle import MineHandle
from base.base_driver import BaseDriver


class MainBusiness:

    def __init__(self, driver):
        self.main_handle = MineHandle(driver)

    def to_login(self):
        self.main_handle.click_login_entrance()

    def to_mine_req(self):
        self.main_handle.click_mine_req_entranc()

    def to_mine_tab(self):
        self.main_handle.click_tab_mine()

    def back_to_mine(self):
        self.main_handle.click_back()










