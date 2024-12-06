f1 = open('Codingal.txt', 'a+')
f2 = open('sample_doc.txt', 'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print("The content of the first file after appending: \n", f1.read())
print("The content of the second file after appending: \n", f2.read())

f1.close()
f2.close()