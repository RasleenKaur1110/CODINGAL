import turtle

turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.left(90)
    i = i + 1

turtle.done()
