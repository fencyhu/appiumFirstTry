# coding=utf-8
from page.home_page import HomePage


class HomeHandle:

    def __init__(self, driver):
        self.home_page = HomePage(driver)

    def get_city_change_alert(self):
        """
        获取切换城市弹窗
        """
        return self.home_page.get_cityChangeArlert_ele()

    def accept_city_change(self):
        """
        根据坐标点击切换到当前城市弹窗中的切换按钮
        """
        coordinate = self.home_page.get_cityChangeAcceptButton_loc()
        x = coordinate[0]
        y = coordinate[1]
        self.driver.tap([(x, y), (x, y)])

    def cancel_city_change(self):
        """
        根据坐标点击切换到当前城市弹窗中的取消按钮
        """
        coordinate = self.home_page.get_cityChangeCancelButton_loc()
        x = coordinate[0]
        y = coordinate[1]
        self.driver.tap([(x, y), (x, y)])

    def click_tab_home(self):
        """
        根据元素点击底部栏"首页"按钮
        """
        self.home_page.get_tab_home().click()
