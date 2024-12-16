with open ('Codingal.txt', 'w') as file:
    file.write("Hi, I am Rasleen. I am 13 years old.")

with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this line are...")
    for line in data:
        word = line.split()
        print(word)