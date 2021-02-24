# coding: utf-8
from ipaddress import *


class NetDevice:
    """Прототип устройства"""

    def __init__(self, ip, community):
        try:
            ip_address(ip)
        except ValueError:
            raise Exception('Не тот ip')
        else:
            self.__ip = ip
        self.__community = community

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
    def community(self):
        return self.__community

    @community.setter
    def community(self, c):
        self.__community = c


class SwitchSnmp(NetDevice):
    """Класс свича"""

    def __init__(self, name, ip, community, mib):
        self.__name = name
        super().__init__(ip, community)
        self.__mib = mib

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def mib(self):
        return self.__mib

    @mib.setter
    def mib(self, m):
        self.__mib = m
