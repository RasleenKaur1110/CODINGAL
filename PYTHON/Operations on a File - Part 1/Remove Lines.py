file1 = open('Codingal.txt', 'r')
file2 = open('Codingal1.txt', 'w')

for line in file1.readlines():
    if not (line.startswith('Coding')):
        file2.write(line)

file1.close()
file2.close()

file3 = open('Codingal1.txt', 'r')
print(file3.read())
file3.close()