a=input("Enter the integers:")
b=list(map(int,a.split()))

for j in range(len(b)):
	if b[j]>100:
		b[j]="over"
print(b)
