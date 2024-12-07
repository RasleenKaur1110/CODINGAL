file = open('Codingal.txt', 'r')
print(file.read)
file.seek(0)

print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('Codingal', 'a')
file.write("Hi, I am Rasleen. I am 13 years old.")
file.close()