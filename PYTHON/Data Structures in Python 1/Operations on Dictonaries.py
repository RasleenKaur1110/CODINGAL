dict = {}

dict = {1: 'mango', 2: 'coding'}

dict = {'name': 'Rasleen', 1: [11, 15, 108]}

dict = {'name': 'Zaara', 'age': 13}

print(dict['name'])
print(dict.get('age'))

dict['age'] = 14
print(dict)

dict['address'] = 'Delhi'
print(dict)

dict.pop('age')
print(dict)

print("Address: ", dict.get('address'))

dict.clear()
print(dict)

