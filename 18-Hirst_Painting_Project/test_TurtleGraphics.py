
import random

# # import everything
# from turtle import *
# # import Turtle from turtle
# from turtle import Turtle

import turtle as t
tim = t.Turtle()

timmy = t.Turtle()
# timmy.shape("turtle")
# timmy.color("blue")

# # create square
# for i in range(4):
#     timmy.right(90)
#     timmy.forward(100)

# # create dashed line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# # triangle to decagon
# for i in range(3,11):
#     tim.color(random.choice(colors))
#     for j in range(i):
#         tim.right(360/i)
#         tim.forward(50)

# # random walk
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
# directions = [0,90,180,270]
# # tim.width(10) or
# tim.pensize(10)
# tim.speed("fastest")
# for i in range(100):
#     # tim.color(random.choice(colors))
#     tim.pencolor(random_color())
#     # tim.right(90*random.choice(directions))
#     tim.setheading(random.choice(directions))
#     tim.forward(30)

# Spirograph
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(80)
        current_heading = tim.heading()
        tim.setheading(current_heading+size_of_gap)
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

# # https://pypi.org/project/heroes/
# # $ pip install heroes
# import heroes
# print(heroes.gen())

