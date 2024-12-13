with open('sample.txt', 'w') as file:
    file.write("Hello, this in line 1. \n")
    file.write("This is line 2. \n")
    file.write("And this line 3. \n")

print("1. Reading the entire file:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

print("\n2. Reading the file line by line:")
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())

print("\n3. Reading all lines as a list:")
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)

print("\n4. Reading specific number of characters:")
with open("sample.txt", "r") as file:
    print(file.read(10))


