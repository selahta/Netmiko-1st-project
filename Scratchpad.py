#!/usr/bin/python3

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

routers = [
     {'device_type': 'cisco_ios',
     'ip': '192.168.1.11',
     'username': 'dtecle',
     'password': getpass()},

     {'device_type': 'cisco_ios',
     'ip': '192.168.1.12',
     'username': 'dtecle',
     'password': getpass()},

     {'device_type': 'cisco_ios',
     'ip': '192.168.1.13',
     'username': 'dtecle',
     'password': getpass()}
]

start = datetime.now()

if routers[0]:
    net = ConnectHandler(**routers[0])
    config = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0', 'exit',
              'ip route 0.0.0.0 0.0.0.0 f0/0',
              'service password-encryption']
    output = net.send_config_set(config)
    print(output)

if routers[1]:
    net = ConnectHandler(**routers[1])
    config = ['int loop 0', 'ip address 2.2.2.2 255.255.255.0', 'exit',
              'ip route 0.0.0.0 0.0.0.0 f0/0',
              'service password-encryption']
    output = net.send_config_set(config)
    print(output)

if routers[2]:
    net = ConnectHandler(**routers[2])
    config = ['int loop 0', 'ip address 3.3.3.3 255.255.255.0', 'exit',
              'ip route 0.0.0.0 0.0.0.0 f0/0',
              'service password-encryption']
    output = net.send_config_set(config)
    print(output)

for device in routers:
    net = ConnectHandler(**device)
    print(net.send_command('write memory'))
    print(net.send_command('show start | include username'))
    print(net.send_command('show ip interface brief | include up'))
    print(net.send_command('show version'))

end = datetime.now()

Total_time = end - start
print(Total_time)

net.disconnect()
