"""EX04 -  Sunset in the Rockies! In this project, I am aim to create the scene of a sunset in the Colorado Rockies."""

__author__ = "730463236"

from turtle import Turtle, colormode, done 
from random import randint
colormode(225)


def main() -> None: 
    """This is the entrypoint for my scene."""    
    sunset: Turtle = Turtle()
    sunset.screen.bgcolor("light blue")
    sunset.speed(50)
    sun_ray(sunset, 0, 190)
    draw_circle(sunset, 0, 90)
    mountain(sunset, -1000, -500)
    """I have called the plane function twice, drawing a plane in two different locations in lines 20 and 22."""
    small_mount(sunset, -1000, -500)
    plane(sunset, 400, 190)
    sunset.right(45)
    plane(sunset, -400, 190)
    sunset.hideturtle()
    done()    


def draw_triangle(sunset: Turtle, x: float, y: float) -> None:
    """This function creates a triangle."""
    c: int = 0
    while c < 3:
        sunset.forward(x)
        sunset.left(y)
        c = c + 1


def draw_circle(sunset: Turtle, x: float, y: float) -> None: 
    """This function creates a circle which represents the sun. It has a yellow border and has an orange filling as shown in line 41."""
    sunset.penup()
    sunset.goto(x, y)
    sunset.pendown()
    sunset.color("yellow", "orange")
    sunset.begin_fill()
    sunset.circle(100)
    sunset.end_fill()


def sun_ray(sunset: Turtle, x: float, y: float) -> None: 
    """This function draws the yellow sun rays that surround the sun."""    
    sunset.pencolor("yellow")
    
    i: int = 0
    while i < 180:
        sunset.penup()
        sunset.goto(x, y)
        sunset.pendown()
        sunset.forward(150)
        sunset.right(2)
        i = i + 1


def mountain(sunset: Turtle, x: float, y: float) -> None: 
    """This function draws a mountain. This is looped so that it creates mountains line like in the Colorado Rockies."""
    i: int = 0 
    sunset.color("brown", "brown")

    while i < 25:
        sunset.penup()
        sunset.goto(x, y)
        sunset.pendown()
        sunset.begin_fill()
        """I call the draw_triangle function to draw the brown mountains in line 72."""
        draw_triangle(sunset, 500, 120)
        sunset.end_fill()
        x = x + 60
        y = y * 1
        i = i + 1
    
    sunset.end_fill()


def small_mount(sunset: Turtle, x: float, y: float) -> None:
    """This function constructs a smaller array of mountains of random sizes."""
    i: int = 0 
    sunset.color("green", "green")
    """I have implemented a loop that draws smaller mountains of random sizes in lines 86-98."""
    while i < 28:
        forw_length: int = randint(250, 450)
        sunset.penup()
        sunset.goto(x, y)
        sunset.pendown()
        sunset.begin_fill()
        """I call the draw_triangle function to draw the small green mountains."""
        draw_triangle(sunset, forw_length, 120)
        sunset.end_fill()
        sunset.penup()
        x = x + 60
        y = y * 1
        i = i + 1  


def plane(sunset: Turtle, x: float, y: float) -> None:
    """This function draws a plane."""
    sunset.pencolor("black")

    sunset.penup()
    sunset.goto(x, y)
    sunset.pendown()
    sunset.forward(220)
    sunset.left(135)
    sunset.forward(30)
    sunset.left(180)
    sunset.forward(30)
    sunset.right(90)
    sunset.forward(30)
        

if __name__ == "__main__":
    main()