#!/usr/bin/python3
from netaddr import *

subnet = input('Please Enter Subnet: ')
ip=IPNetwork(subnet)
print(ip)
