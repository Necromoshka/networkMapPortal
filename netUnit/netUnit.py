from .netDevice import *
from pysnmp.hlapi import *


class SwitchSnmp(NetDevice):
    """Класс свича"""

    def __init__(self, name, ip, community):
        self.__community = community
        super().__init__(ip, name)
        self.__port = 161
        self.__oid = '.1.3.6.1.2.1.2.2.1.2'
        self.__varBinds = []

    @property
    def community(self):
        return self.__community

    @community.setter
    def community(self, c):
        self.__community = c

    def __snmp_getcmd(self):
        return (getCmd(SnmpEngine(),
                       CommunityData(self.__community),
                       UdpTransportTarget((super().ip, self.__port)),
                       ContextData(),
                       ObjectType(ObjectIdentity(self.__oid))))

    def __snmp_get_next(self):
        self.__varBinds = next(self.__snmp_getcmd())
        return self.__varBinds


    @property
    def sw_port(self):
        port = 0
        return port, self.__snmp_get_next()
