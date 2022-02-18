from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__() # inherits from the Turtle class
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """New Food location"""
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)