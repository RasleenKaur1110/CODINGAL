class Intro:
    species = "robot"
    def __init__(self, name, age, hobby, role):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.role = role

tom = Intro("Tom", 5, "Coding", "an assistant in building new robots")
jerry = Intro("Jerry", 6, "Reading books", "a librarian in the robot knowledge base")

print("Hi Everyone, I am {}, and I am a {}.".format(tom.name, tom.species))
print("I am {} years old.".format(tom.age))
print("My favourite hobby is {}.".format(tom.hobby))
print("I work as {}.".format(tom.role))

print("Hi Everyone, I am {}, and I am a {}.".format(jerry.name, jerry.species))
print("I am {} years old.".format(jerry.age))
print("My favourite hobby is {}.".format(jerry.hobby))
print("I work as {}.".format(jerry.role))
