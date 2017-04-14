#!/usr/bin/python3
from netmiko import ConnectHandler
from getpass import getpass

username='cisco'
password='cisco'
ip='10.50.5.57'
list=[]
conn = ConnectHandler(device_type='cisco_ios',ip=ip, username=username, password=password)
stdout = conn.send_command('show interfaces description')
for i in stdout.splitlines():
#	print(i.split())
#	print("ikinci")
	list.append(i.split())	


for i in list:
	if len(i)==4 and "Gi" in i[0]:
		print(i[0],i[3])

#print(list)	
