#Add 'ing' at the end of a give string if it already ends with 'ing',then add 'ly'.
s = input("Enter a string: ")
if s.endswith("ing"):
    s = s + "ly"
else:
    s = s + "ing"
print("Result =", s)

