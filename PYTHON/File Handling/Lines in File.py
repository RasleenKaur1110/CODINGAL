file = open('Codingal.txt', 'r')
Counter = 0

Content = file.read()
Colist = Content.split(".")

for i in Colist:
    if i:
        Counter += 1

print("No. of lines in the file")
print(Counter)