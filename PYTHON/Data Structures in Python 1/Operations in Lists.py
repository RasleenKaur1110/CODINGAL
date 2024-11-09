list = ['Apple', 'Mango', 'Watermelon', 'Banana', 'Guava']

print("Length of the list: ", len(list))
print("First Element:", list[0])
print("Last Element: ", list[-1])

list.append('Papaya')
print("Updated list: ", list)

list.remove('Guava')
print("Updated list: ", list)

list.sort()
print("Sorted list: ", list)

list.pop(1)
print("Updated list: ", list)

list.reverse()
print("Reversed list: ", list)

print("Multiplication on list: ", list*2)

list = list[:4]
print("Sliced list: ", list)

list.clear()
print("Updated list: ", list)