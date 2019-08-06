# coding=utf-8
import multiprocessing
import main.test_suite
from util.server import Server
from util.write_user_command import WriteUserCmd


def start_process(target, threads_num):
    for i in range(threads_num):
        print "执行进程---" + str(i)
        t = multiprocessing.Process(target=target, args=(i,))
        t.start()


def run():
    server = Server()
    write_user_cmd = WriteUserCmd()
    server.start_server()
    print "完成start_server()"
    devices_length = write_user_cmd.get_file_lines()
    start_process(main.test_suite.run_suite, devices_length)

"""
为了让它显眼一点加个注释
"""
run()
