#Form a list of vowels from a given word
word=input("Enter a word:")
vowels=[]
for ch in word:
	if ch.lower() in "aeiou":
		vowels.append(ch)
print("List of vowels:",vowels)
