import turtle

# Initialize the turtle
t = turtle.Turtle()

# Set the turtle's speed
t.speed(0)

# Draw the Apple logo
t.begin_fill()
t.fillcolor("red")
t.pencolor("green")
t.left(155)
for i in range(205):
    t.forward(1)
    t.left(1)
for i in range(18):
    t.forward(1)
    t.left(1)
for i in range(20):
    t.forward(1)
    t.right(1)
for i in range(18):
    t.forward(1)
    t.left(1)
for i in range(205):
    t.forward(1)
    t.left(1)
t.end_fill()

t.penup()
t.setposition(-10,6)
t.pendown()
t.begin_fill()
for i in range(1):
    t.forward(1)
t.end_fill()

for i in range(15):
    t.forward(10)
    t.right(10)

# Draw the Apple text
t.penup()
t.setposition(-100, 0)
t.pendown()
t.write("Apple", font=("Arial", 20, "bold"))

# Exit the turtle graphics
turtle.done()
ImportError