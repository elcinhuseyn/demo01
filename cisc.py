import paramiko
from getpass import getpass

username='cisco'
password=getpass()

sws = ['10.50.5.55','10.50.5.57','10.50.5.111']
info = 'System seial number'

def cisco_con(ip, username, password):
	conn = paramiko.SSHClient()
	conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	conn.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False, timeout=5)
	stdin, stdout, stderr = conn.exec_command('show version | inc System serial number')
	for i in stdout:
		line = i.rstrip()
		print(line)

for i in sws:
	try:
		print('Cisco switch:', i)
		cisco_con(i,username=username,password=password)
	except:
		print('Wrong ip')
