# coding=utf-8
'''
import multiprocessing
from util.server import Server


def target(i):
    print "我是方法---", str(i)
    Server().start_server()


threads = []
for i in range(2):
    print "创建线程---" + str(i)
    t = multiprocessing.Process(target=target, args=(i,))
    threads.append(t)
for j in threads:
    print "执行进程---" + str(j)
    j.start()

'''

import unittest
import HTMLTestRunner
from case.mine_test import CaseTest
import os
from util.server import Server


def run_suite(i):
    current_path = os.path.dirname(__file__)
    html_file = current_path+"/report/report"+str(i)+".html"
    fp = open(html_file, "wb")
    HTMLTestRunner.HTMLTestRunner(fp).run(get_suite(i))


def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_to_my_req", parame=i))
    suite.addTest(CaseTest("test_to_login", parame=i))
    print "suite--"+str(i), suite
    return suite


Server.start_server()
run_suite(0)
