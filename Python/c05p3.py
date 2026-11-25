import csv

file = open("students.csv")
reader = csv.reader(file)

for row in reader:
    print(row)

file.close()


""" 
import csv

filename = "students.csv"

try:
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)              

except FileNotFoundError:
    print("File not found:", filename)

"""
