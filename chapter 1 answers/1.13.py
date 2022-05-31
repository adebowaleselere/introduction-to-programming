import turtle

# This is to render the vertical cross
turtle.penup()
turtle.goto(50, 0)
turtle.right(90)
turtle.pendown()
turtle.forward(100)

# This is to render the horizontal cross
turtle.penup()
turtle.goto(0, -50)
turtle.right(270)
turtle.pendown()
turtle.forward(100)

# This is just to move the pen away
turtle.penup()
turtle.goto(0, 0)


turtle.done()
