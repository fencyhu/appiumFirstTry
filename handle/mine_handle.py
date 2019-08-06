# coding=utf-8
from page.mine_page import MinePage


class MineHandle:

    def __init__(self, driver):
        self.mine_page = MinePage(driver)

    def click_tab_mine(self):
        """
        根据元素点击底部栏"我的"按钮
        """
        element = self.mine_page.get_tab_mine()
        if element is None:
            return
        element.click()

    def click_login_entrance(self):
        """
        根据元素点击"去登陆"按钮
        """
        self.mine_page.get_login_entrance().click()

    def click_mine_req_entranc(self):
        """
        根据元素点击"我的需求"按钮
        """
        self.mine_page.get_mine_req_entrance().click()

    def click_back(self):
        """
        根据元素点击"返回"按钮
        """
        self.mine_page.get_back_button().click()
