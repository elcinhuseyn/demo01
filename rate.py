#!/usr/bin/python3
a=float(input("Enter Hours:"))
b=float(input("Enter Rate:"))
def computepay(x,y):
	if x>40:
		pay=(40*y)+((x-40)*(y*1.5))
		print(pay)
	else:
		pay=x*y
		print(pay)
computepay(a,b)
