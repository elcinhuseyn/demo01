x#!/usr/bin/python3
a=open('bigfile.txt','r')
b=a.read()
c=b.split()
#print(c)
d=dict()
for i in c:
        d[i]=d.get(i,0)+1
print(d)
#bigc=None
#bigw=None
#for i,c in d.items():
#       if bigc is None or c>bigc:
#               bigc=c
#               bigw=i
#print(bigw,bigc)
#n=open('new.txt','w')
#for k,v in d.items():
#	if v>=max(d.values()):
#	for k in c:
#		v=c.count(k)	
#	n.write(k)
#	n.write('-')
#	n.write(str(v))
#	n.write('\n')
#		del d[k]
#n.close
