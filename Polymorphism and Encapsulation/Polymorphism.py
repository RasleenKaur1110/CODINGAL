class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

cat1 = Cat("Tyler", 5)
dog1 = Dog("Tyson", 3)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.intro()

