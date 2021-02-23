# coding: utf-8
from ipaddress import *


class NetDevice:
    """Прототип устройства"""

    def __init__(self, ip, comunity):
        self.__ip = ip
        self.__comunity = comunity

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
