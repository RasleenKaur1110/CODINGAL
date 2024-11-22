class Student:
    grade = 8
    name = "Rasleen"

    def intro(self):
        print("Hi, I am a student")
    def details(self):
        print("My name is ", self.name)
        print("I study in grade ", self.grade)

ob = Student()
ob.intro()
ob.details()