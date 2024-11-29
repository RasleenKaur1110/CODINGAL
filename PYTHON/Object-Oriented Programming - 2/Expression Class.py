class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_sum(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {result}")

    def __del__(self):
        print("The object is being deleted.")

expression1 = Expression(11, 15, 18)
expression1.calculate_sum()

expression2 = Expression(7, 22, 8)
expression2.calculate_sum()

del expression1