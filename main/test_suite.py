# coding=utf-8

import unittest
import HTMLTestRunner
from case.mine_test import CaseTest
import os


def run_suite(i):
    current_path = os.path.dirname(__file__)
    html_file = current_path+"/../report/report"+str(i)+".html"
    fp = open(html_file, "wb")
    HTMLTestRunner.HTMLTestRunner(fp).run(get_suite(i))


def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_to_my_req", parame=i))
    suite.addTest(CaseTest("test_to_login", parame=i))
    print "suite--"+str(i), suite
    return suite

