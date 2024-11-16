set = {1, 1, 2, 3, 4, 4, 4}
print("Set:", set)

set.add(5)
print("Updated Set: ", set)

set1 = set
set2 = {2, 4, 5, 6, 6}

print("Difference")
print(set1.difference(set2))
print("Symmetric Difference")
print(set1.symmetric_difference(set2))