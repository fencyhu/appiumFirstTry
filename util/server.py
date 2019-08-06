# coding=utf-8
import datetime
import time

from terminal_cmd import TerminalCmd
from port import Port
from write_user_command import WriteUserCmd


class Server:

    def __init__(self):
        self.cmd = TerminalCmd()
        self.write_user_cmd = WriteUserCmd()

    def get_ios_devices(self):
        devices_list = self.cmd.excute_cmd_result("idevice_id -l |sort -u")
        if len(devices_list) == 0:
            return None
        return devices_list

    def get_port_list(self, devices_list):
        port = Port()
        port_list = port.create_port_list(4700, devices_list)
        return port_list

    def create_command_list(self):
        devices_list = self.get_ios_devices()
        port_list = self.get_port_list(devices_list)
        command_list = []
        for i in range(len(port_list)):
            # command后面加上" &"把命令放入后台执行就不会阻塞程序运行
            command = "appium -p "+str(port_list[i])+" --no-reset --session-override --log ../log/test_"+str(devices_list[i])+".log &"
            command_list.append(command)
            self.write_user_cmd.write_value(self.write_user_cmd.join_data(i, str(port_list[i]), devices_list[i]))
        return command_list

    def start_server(self):
        self.write_user_cmd.clear_data()
        self.kill_server()
        start_list = self.create_command_list()
        for i in start_list:
            print datetime.datetime.now(), "开始启动appium-"+str(i)
            self.cmd.excute_cmd(i)
            print datetime.datetime.now(), "启动appium完成"
        time.sleep(20)

    def kill_server(self):
        command = "ps -A | grep bin/appium |grep -v 'grep bin/appium' | awk '{print $1}'| xargs kill -9"
        self.cmd.excute_cmd(command)

    def finish_process(self, p):
        p.terminate()

if __name__ == "__main__":
    server = Server()
    print server.start_server()
