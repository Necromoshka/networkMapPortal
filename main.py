from netUnit.netUnit import SwitchSnmp

sw = SwitchSnmp('SWA1/1', '192.168.200.26', 'public', '.*V.*')
print(sw.sw_port)
