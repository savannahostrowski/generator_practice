l1=[1,2,3]
l2=[4,5,6]

def generatorConcatenate(lst1, lst2):
	for x in lst1:
		yield x
	for y in lst2:
		yield y


for x in generatorConcatenate(generatorConcatenate(l1,l2),
 															generatorConcatenate(l1,l2)): 
	print(x)


