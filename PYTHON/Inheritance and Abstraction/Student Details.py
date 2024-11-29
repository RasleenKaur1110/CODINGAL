class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(self.fname)
        print(self.lname)

class Student(Person):
    def __init__(self, fname, lname, year):
        self.year = year
        
        super().__init__(fname, lname)

s = Student('Rasleen', 'Kaur', 2030)
s.display()
print(s.year)