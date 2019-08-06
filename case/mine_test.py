# coding=utf-8
from base.base_driver import BaseDriver
import unittest
import time
from business.mine_business import MainBusiness
import HTMLTestRunner
import util.globalvar as gl


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame

class CaseTest(ParameTestCase):

    @classmethod
    def setUpClass(cls):
        base_driver = BaseDriver()
        print parames
        cls.driver = base_driver.ios_driver(parames)

    def setUp(self):
        print "this is setUp"

    def test_to_my_req(self):
        mine_bus = MainBusiness(self.driver)
        print "开始-test_to_my_req"
        mine_bus.to_mine_tab()
        time.sleep(1)
        mine_bus.to_mine_req()
        time.sleep(2)
        mine_bus.back_to_mine()
        time.sleep(1)

#    @unittest.skip("CaseTest")
    def test_to_login(self):
        mine_bus = MainBusiness(self.driver)
        print "开始-test_to_login"
        mine_bus.to_mine_tab()
        mine_bus.to_login()
        time.sleep(1)

    def tearDown(self):
        print "this is tearDown"

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass---cls.driver.quit()"
#        list = gl.get_value("appiumlist")
#        print "tearDownClass---appiumlist="+list
        cls.driver.quit()
#        print "tearDownClass---appiumlist="
#        print "tearDownClass---appiumlist="+process_nums[parames]
#        process_nums[parames].terminate


if __name__ == "__main__":
    #    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_to_my_req"))
    suite.addTest(CaseTest("test_to_login"))
    html_file = "../report/report.html"
    fp = open(html_file, "wb")
    HTMLTestRunner.HTMLTestRunner(fp).run(suite)
