import turtle

# This is the code to render the first square
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# This is the code to  render the vertical center line
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)

# This is the code to render the horizontal center line

turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)

# this is to move the pen away
turtle.penup()
turtle.goto(-10, 0)

turtle.done()
