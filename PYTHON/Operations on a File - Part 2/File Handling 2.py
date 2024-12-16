new = open('New file.txt', 'x')
new.close()

import os
print("Checking if my_file exists or not")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

my_file = open("my_file.txt", 'w')
my_file.write("Hi, I am Rasleen. I am 13 years old.")
my_file.close()

os.remove("Codingal.txt")
os.rmdir("Folder")