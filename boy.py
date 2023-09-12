import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw the first boy
t.penup()
t.goto(-100, 0)
t.pendown()
t.circle(50)
t.penup()
t.goto(-100, -50)
t.pendown()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

# Draw the second boy
t.penup()
t.goto(100, 0)
t.pendown()
t.circle(50)
t.penup()
t.goto(100, -50)
t.pendown()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

# Save the drawing
t.getscreen().getcanvas().postscript(file='C:/Users/jiang/desktop/boys_playing.eps')
