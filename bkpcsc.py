#!/usr/bin/python3

import paramiko
from getpass import getpass

username='cisco'
password=getpass()

sws = ['10.50.5.57','10.50.5.111']
info = 'System seial number'

def cisco_con(ip, username, password):
        backup=open('backup_%s.txt' % str(ip),'a')
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False, timeout=5)
        stdin, stdout, stderr = conn.exec_command('show run')
        for i in stdout:
                line = i.rstrip()
                backup.write(line)
                backup.write('\n') 
        print('backup_%s.txt file created in current directory' % str(ip))

def cisco_cpu(ip, username, password):
        cpu=open('Utilization.txt','a')   
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False, timeout=5)
        stdin, stdout, stderr = conn.exec_command('show processes cpu')
        for i in stdout:
                if i.startswith('CPU'):
                        a=i.split()
                        print("CPU utilization for one minutute is ",a[8])                              
                        if int(a[8].split('%')[0])>20:
                                cpu.write(ip)
                                cpu.write('\n')


for i in sws:
        try:
                print('Cisco switch:', i)
                cisco_con(i,username=username,password=password)
                cisco_cpu(i,username=username,password=password)
        except:
                print('Wrong ip')
