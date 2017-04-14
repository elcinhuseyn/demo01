a=input("Enter File:")
def saysetir(w):
	file=open(w)
	cst=0
	for line in file:
		cst=cst+1
	print('Entered file has ',cst,' line')
	file.close
def sayletter(w):
	file=open(w)
	file01=file.read()
	cltt=0
	for letter in file01:
		if letter.isalpha():
			cltt=cltt+1
	print('Entered file has ',cltt,' letter')
	file.close
def saynum(w):
	file=open(w)
	file01=file.read()
	cnum=0
	for num in file01:
		if num.isdigit():
			cnum=cnum+1
	print('Entered file has ',cnum,' number')
	file.close
def sayspace(w):
	file=open(w)
	file01=file.read()
	csp=0
	for sp in file01:
		if sp.isspace():
			csp=csp+1
	print('Entered file has ',csp,' space')
	file.close

saysetir(a)
sayletter(a)
saynum(a)
sayspace(a)
	
