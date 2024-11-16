#Empty Tuple
tuple1 = ()
print(tuple1)

#Tuple having integers
tuple2 = (1, 2, 3)
print(tuple2)

#Tuple with mixed datatypes
tuple3 = (1, "Hi", 11.5)
print(tuple3)

#Nested Tuple
tuple4 = ("dog", [2, 4, 6], (1, 3, 5))
print(tuple4)

#Accessing tuple elementsusing indexing
tuple5 = ('p', 'e', 'r', 'm', 'i', 't')
print(tuple5[0])
print(tuple5[5])

#Nested tuple
tuple6 = ("Cat", [8, 4, 6], (1, 5, 7))
print(tuple6[0][2])
print(tuple6[1][1])

#Sliced
print("SLICED: ", tuple6[1:4])

#Iterating through tuple
for letter in (tuple5):
    print("Hi", letter)