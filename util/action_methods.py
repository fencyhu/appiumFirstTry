# coding=utf-8
import time

from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal


class ActionMethod:

    def __init__(self):
        base_driver = BaseDriver()
        self.driver = base_driver.ios_driver()
        self.get_by_local = GetByLocal(self.driver)
        self.size = self.get_size()

    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_up(self):
        x1 = self.size()[0] / 2
        y1 = self.size()[1] / 10 * 9
        y2 = self.size()[1] / 10
        self.driver.swipe(x1, y1, 0, y2 - y1, 500)

    def swipe_down(self):
        x1 = self.size()[0] / 2
        y1 = self.size()[1] / 10
        y2 = self.size()[1] / 10 * 9
        self.driver.swipe(x1, y1, 0, y2 - y1, 500)

    def swipe_left(self):
        x1 = self.size[0] / 10 * 9
        x2 = self.size[0] / 10
        y1 = self.size[1] / 2
        self.driver.swipe(x1, y1, x2 - x1, 0, 500)

    def swipe_right(self):
        x1 = self.size[0] / 10
        x2 = self.size[0] / 10 * 9
        y1 = self.size[1] / 2
        self.driver.swipe(x1, y1, x2, 0, 500)

    #    self.driver.execute_script("mobile:dragFromToForDuration",
    #                          {"duration": 0.5, "element": None, "fromX": x1, "fromY": y1, "toX": x2, "toY": y1})

    def swipe(self, direction):
        if direction == "up":
            self.swipe_up()
        elif direction == "down":
            self.swipe_down()
        elif direction == "right":
            self.swipe_right()
        else:
            self.swipe_left()

    def on_click(self, *args):
        """
        元素点击
        key
        """
        element = self.get_by_local.get_element(args[0], args[1])
        print "element", element
        if element is None:
            print args[0], "元素没找到"
            return args[0], "元素没找到"
        element.click()

    def on_tap(self, *args):
        """
        坐标点击
        key
        """
        coordinate = self.get_by_local.get_coordinate(args[0], args[1])
        print "coordinate", coordinate
        if coordinate is None:
            return args[0], "坐标没找到"
        self.driver.tap([(coordinate[0],coordinate[1]),(coordinate[0],coordinate[1])])

    def input(self, *args):
        """
        输入
        key,value
        """
        element = self.get_by_local.get_element(args[0])
        if element is None:
            return args[0], "元素没找到"
        element.send_keys(args[1])


