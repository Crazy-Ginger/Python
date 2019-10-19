import turtle
import numpy
import math

window = turtle.Screen()
alex = turtle.Turtle()
alex.speed(10)
alex.pensize(1)
x = 3
i =20
def run_again(x,i):
        alex.forward(5)
        alex.right(x)
        x = x + 1
        i = i +2
        run_again(x,i)
run_again(x,i)
