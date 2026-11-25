a = input("Enter the integers: ")
b = list(map(int, a.split()))
c = []

for i in range(len(b)):
    if b[i] > 0:
        c.append(b[i])

print(c)

