#count the occurrence of each word in a line of text
line = input("Enter the line: ")
words = line.split()

for word in set(words):
    print(word, ":", words.count(word))


