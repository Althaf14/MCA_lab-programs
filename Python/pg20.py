a = input("Enter first colors: ").split(',')
b = input("Enter second colors: ").split(',')

for x in a:
    if x not in b:
        print(x)

