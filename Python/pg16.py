  list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))

print("\nList 1:", list1)
print("List 2:", list2)

if len(list1) == len(list2):
    print("a) Both lists have the same length.")
else:
    print("a) Lists do not have the same length.")

if sum(list1) == sum(list2):
    print("b) Both lists have the same sum.")
else:
    print("b) Lists do not have the same sum.")

common = set(list1).intersection(set(list2))

if common:
    print("c) Common elements:", common)
else:
    print("c) There are no common elements.")

