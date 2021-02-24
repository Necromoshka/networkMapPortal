# coding: utf-8
from ipaddress import *


class NetDevice:
    """Прототип устройства"""

    def __init__(self, ip, name):
        try:
            ip_address(ip)
        except ValueError:
            raise Exception('Не тот ip')
        else:
            self.__ip = ip
        self.__name = name

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, i):
        try:
            ip_address(i)
        except ValueError:
            raise Exception('Не тот ip')
        else:
            self.__ip = i

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

