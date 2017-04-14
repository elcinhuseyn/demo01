#!/usr/bin/python3
from random import randint
oldlist=[]
for i in range(20): oldlist.append(randint(1,20))
print("This is random list: ",oldlist)
new_list = []
while oldlist:
    minimum = oldlist[0]
    for x in oldlist: 
        if x < minimum:
            minimum = x
    print(x,"min: ", minimum)
    new_list.append(minimum)
    print(new_list)
    oldlist.remove(minimum)    
print(new_list)
