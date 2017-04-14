!/usr/bin/env python3

mbox = open('mbox-short.txt')
box=open('box','w+')
for line in mbox:
    line = line.rstrip()
    if line.startswith('From '):        
        a=line.split()
        b=a[5]
        c=b.split(':')[0]
#        print(c)
        box.write(c)
        box.write(' ')
box.close()
e=open('box')
d=e.read()
print(type(d))
e.close()
f=d.split()
print(f)
count=0
newl=[]
while f:
	blc=f[0]
	for i in f:
#		i=int(i)
		if i<blc:
			blc=i
			newl.append(blc)
			f.remove(i)
print(newl)
#	print(f)
