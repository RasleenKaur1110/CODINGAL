def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1, 'Rasleen', 'VIII'], [2, 'Zaara', 'VII'], [3, 'Rakshit', 'VI'], [4, 'Samreen', 'V'], [5, 'Chhavi', 'IV']]

print("Original list: ")
print(students)
print("List converted into dictonary: ")
print(test(students))
