output = open("UpdatedFile.txt", 'w')
input = open("C:/Users/Samsung/Desktop/CODINGAL/PYTHON/Operations on a File - Part 2/Repeated.txt", 'r')

lines = set()
print("Eliminating duplicate lines...")
for line in input:
    if line not in lines:
        output.write(line)
        lines.add(line)

input.close()

output.close()
file = open("UpdatedFile.txt", 'r')
print(file)
