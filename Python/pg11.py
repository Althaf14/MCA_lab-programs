#Display future leap years from the current year to a final year entered by user 
cyear = int(input("Enter the current year: "))
nyear = int(input("Enter the limit: "))

for i in range(cyear, nyear):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(i)
