import re
import sys
import winreg
from itertools import count
from constants import PATH, NAME, REGX


class InfoRegistry:
    def __init__(self):
        self.key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            PATH,
            0,
            winreg.KEY_READ)

    def collection_info(self):
        value, _ = winreg.QueryValueEx(self.key, NAME)
        result = []
        list_of_names = []

        for i in count():
            try:
                name, val, _ = winreg.EnumValue(self.key, i)
                if name != NAME and val == value:
                    list_of_names.append(name)
                    result.append(search(REGX, name).group(1))
                    break
            except OSError:
                break

        return (list_of_names, result)


def main():
    inf = InfoRegistry()
    print(inf.collection_info()[0])
    print(inf.collection_info()[1])


if __name__ == '__main__':
    pass
