from .netDevice import *
from pysnmp.entity.rfc3413.oneliner import cmdgen
import re


class SwitchSnmp(NetDevice):
    """Класс свича"""

    def __init__(self, name, ip, community, ret):
        self.__community = community
        super().__init__(ip, name)
        self.__port = 161
        self.__oid = '.1.3.6.1.2.1.2.2.1.2' #1.3.6.1.2.1.17.4.3.1.1
        self.__varBinds = []
        self.__cmdGen = cmdgen.CommandGenerator()
        self.__out = {}
        self.__r = re.compile(ret)  # .*F.*  #([0-9A-Fa-f]{2}[:]){5}[0-9A-Fa-f]{2}

    @property
    def community(self):
        return self.__community

    @community.setter
    def community(self, c):
        self.__community = c

    def __snmp_walk(self):
        eradication, error_status, error_index, var_bind_table = self.__cmdGen.nextCmd(cmdgen.CommunityData(
                                                                                               self.__community),
                                                                                       cmdgen.UdpTransportTarget(
                                                                                           (self.ip, self.__port)),
                                                                                       self.__oid)
        if eradication:
            print(eradication)
        else:
            if error_status:
                print('%s at %s' % (
                    error_status.prettyPrint(),
                    error_index and var_bind_table[-1][int(error_index) - 1] or '?'
                )
                      )
            else:
                for varBindTableRow in var_bind_table:
                    for name, val in varBindTableRow:
                        self.__out[name.prettyPrint()] = val.prettyPrint()

        return self.__out

    @property
    def sw_port(self):
        o = self.__snmp_walk()
        s = []
        for z in o:
            st = ''
            for x in o[z]:
                st = st + x
            if self.__r.search(st):
                s.append('%s = %s' % (z, st))
        return s
