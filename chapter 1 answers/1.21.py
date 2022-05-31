import turtle

turtle.penup()
turtle.goto(0, -92)
turtle.pendown()

turtle.circle(100)

turtle.penup()
turtle.goto(0, 90)
turtle.pendown()
turtle.write("12")

turtle.penup()
turtle.goto(90, 0)
turtle.pendown()
turtle.write("3")

turtle.penup()
turtle.goto(-90, 0)
turtle.pendown()
turtle.write("6")

turtle.penup()
turtle.goto(0, -90)
turtle.pendown()
turtle.write("9")

# Minute hand
turtle.penup()
# turtle.color("red")
turtle.pensize(2)
turtle.goto(0, 6)
turtle.pendown()
turtle.forward(70)


# Second hand
turtle.penup()
turtle.color("red")
turtle.pensize(1)
turtle.goto(0, 6)
turtle.pendown()
turtle.left(90)
turtle.forward(70)

# Hour hand
turtle.penup()
turtle.color("black")
turtle.pensize(3)
turtle.goto(0, 6)
turtle.pendown()
turtle.left(90)
turtle.forward(50)

turtle.done()
