# coding=utf-8
import os
import yaml


class WriteUserCmd:
    def __init__(self):
        current_path = os.path.dirname(__file__)
        self.file_path = current_path+"/../config/userconfig.yaml"

    def read_data(self, file_path=None):
        if file_path is None:
            file_path = self.file_path
        with open(file_path) as fr:
            file_data = yaml.load(fr, Loader=yaml.FullLoader)
        return file_data

    def get_value(self, key, child_key):
        data = self.read_data()
        value = data[key][child_key]
        return value

    def write_value(self, data, file_path=None):
        if file_path is None:
            file_path = self.file_path
        with open(file_path, "a") as fr:
            yaml.dump(data, fr)

    def join_data(self, i, port, device):
        data = {
            "user_info_"+str(i): {
                "port": port,
                "deviceId": device
            }
        }
        return data

    def clear_data(self, file_path=None):
        if file_path is None:
            file_path = self.file_path
        with open(file_path, "w") as fr:
            fr.truncate()
        fr.close()

    def get_file_lines(self):
        data = self.read_data()
        return len(data)


if __name__ == "__main__":
    wu = WriteUserCmd()
    print wu.write_value(wu.join_data(6, 4706, "id06"))




