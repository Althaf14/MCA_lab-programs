file = open("sample.txt")
lines = []

for line in file:
    lines.append(line.strip())

file.close()
print(lines)
"""
filename = "sample.txt"
lines = []

try:
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.strip())      

    print("File contents stored in list:")
    print(lines)

    print("\nLine by line:")
    for i, line in enumerate(lines, start=1):
        print(i, ":", line)

except FileNotFoundError:
    print("File not found:", filename)


"""
