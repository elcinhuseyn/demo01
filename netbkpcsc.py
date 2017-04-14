#!/usr/bin/python3
from netmiko import ConnectHandler
from getpass import getpass

username='cisco'
password=getpass()

sws = ['10.50.5.57','10.50.5.111']
info = 'System seial number'

def cisco_con(ip, username, password):
        backup=open('netbackup_%s.txt' % str(ip),'a')
        conn = ConnectHandler(device_type='cisco_ios',ip=ip, username=username, password=password)
        stdout = conn.send_command('show run')
        backup.write(stdout)
        backup.write('\n') 
        print('backup_%s.txt file created in current directory' % str(ip))

def cisco_cpu(ip, username, password):
        cpu=open('NetUtilization.txt','a')   
        conn = ConnectHandler(device_type='cisco_ios',ip=ip, username=username, password=password)
        stdout = conn.send_command('show processes cpu')
        list=stdout.split()
        print("CPU utilization for one minutute is ",list[8])  
        if int(list[8].split('%')[0])>20:
            cpu.write(ip)
            cpu.write('\n')


for i in sws:
        try:
                print('Cisco switch:', i)
                cisco_con(i,username=username,password=password)
                cisco_cpu(i,username=username,password=password)
        except:
                print('Wrong ip')
