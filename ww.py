
#!/usr/bin/python3
from random import randint
newlist=[]
for i in range(20): newlist.append(randint(1,20))
print("This is random list: ",newlist)
srtl=[]
aa=newlist[0]
for i in newlist:
	if i < aa:
		aa=i
srtl.append(aa)	
newlist.remove(aa)
print(srtl)	


#aa=sorted(newlist)
#print("\nThis is sorted list: ",aa)
