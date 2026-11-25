a=int(input("Enter the limit: "))
n1=0
n2=1
for i in range(n1,a):
	print(n1,end=",")
	n1,n2=n2,n1+n2
