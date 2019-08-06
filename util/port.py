# coding=utf-8
from terminal_cmd import TerminalCmd

class Port:
    def __init__(self):
        self.cmd = TerminalCmd()

    def port_not_used(self, port_num):
        command = "lsof -i tcp:"+str(port_num)
        result = self.cmd.excute_cmd_result(command)
        flag = True if len(result) == 0 else False
        return flag

    def create_port_list(self, start_port, devices_list):
        port_list = []
        if devices_list is not None:
            while len(port_list) != len(devices_list):
                if self.port_not_used(start_port):
                    port_list.append(start_port)
                start_port += 1
        else:
            print "设备列表为空，生成端口失败！"
        return port_list

