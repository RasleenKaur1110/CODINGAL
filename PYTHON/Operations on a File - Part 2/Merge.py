with open('Codingal.txt') as fp:
    data1= fp.read()
with open("Sample.txt") as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2
print("Merging two files...")
with open("Merge.file.txt", 'w') as fp:
    fp.write(data1)