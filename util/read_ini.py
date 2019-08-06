# coding=utf-8
import ConfigParser
import os


class ReadIni:
    def __init__(self, file_path=None):
        current_path = os.path.dirname(__file__)
        if file_path is None:
            self.file_path = current_path+'/../config/LocalElement.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_data = ConfigParser.ConfigParser()
        read_data.read(self.file_path)
        return read_data

    def get_value(self, key, section):
        """
        通过key获取对应的value
        :param key:
        :param section:
        :return:
        """
        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value


if __name__ == '__main__':
    read_ini = ReadIni()
    print read_ini.file_path
    print read_ini.get_value("tabBar_Account", "home_element")
