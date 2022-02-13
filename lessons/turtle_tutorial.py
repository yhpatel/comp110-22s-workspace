"""Turtle Tutorial"""


from turtle import Turtle, colormode, done 
colormode(225)
leo: Turtle = Turtle()
bob: Turtle = Turtle()

leo.penup()
leo.goto(0, 0)
leo.pendown()
bob.penup()
bob.goto(0, 0)
bob.pendown()

leo.color("red", "yellow")
bob.pencolor("gray")
 
leo.speed(50)
bob.speed(100)
leo.begin_fill()

side_length: int = 300
i: int = 0 
while(i < 3): 
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
leo.end_fill()

leo.hideturtle()

i: int = 0
while (i < 45):
    side_length = side_length * 1
    bob.forward(side_length)
    bob.left(120.5)
    i = i + 1
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
done()