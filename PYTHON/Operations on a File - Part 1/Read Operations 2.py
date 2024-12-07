file = open('Codingal.txt', 'r')
print("Single time")
print(file.readline())
file.close()

file = open('Codingal.txt')
print("Multiple times")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('Codingal.txt')
print("In Loop")
for line in file:
    print(line)
file.close()
