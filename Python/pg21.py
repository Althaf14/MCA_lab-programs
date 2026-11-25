d = {}
n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value
print("Ascending:", dict(sorted(d.items())))
print("Descending:", dict(sorted(d.items(), reverse=True)))

