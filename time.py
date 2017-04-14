#!/usr/bin/python3

mbox = open('mbox-short.txt')
time=[]
for line in mbox:
    line = line.rstrip()
    if line.startswith('From '):        
        a=line.split()[5]
        b=a.split(':')[0]
        time.append(b)
def rem_dub(list,val):
	while val in list:
		list.remove(val)
while time:
	for i in time:
		if i==min(time):
			print(i," ",time.count(i))
			rem_dub(time,i)
