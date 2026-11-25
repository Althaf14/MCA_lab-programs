#create a string from given string where first and last characters exchange.
s=input("Enter a string :")
a=list(s)
a[0],a[-1]=a[-1],a[0]
print("".join(a))
#other
#create a string from given string where first and last characters exchange.
"""s = input("Enter a string :")
a = list(s)

a[0], a[-1] = a[-1], a[0]

for ch in a:
    print(ch, end="")"""

