import turtle
import time
from operator import truediv

screen=turtle.Screen()
screen.bgcolor("white")

ball=turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()

y_speed=10
gravity=-1

while True:
    y_speed+=gravity
    ball.sety((ball.ycor() + y_speed))

    if ball.ycor() < -100:
        y_speed = 10
        time.sleep(0.05)





# Normal line
import turtle
t=turtle.Turtle()
t.forward(100)
turtle.done()




# Turtle line
import turtle
t=turtle.Turtle()

t.shape("turtle")
t.color("red")
t.pensize(4)
t.forward(100)
turtle.done()




# star programm
import turtle
t=turtle.Turtle()
t.speed(1)

for i in range(5):
    t.forward(100)
    t.right(144)



# triangle programm
import turtle

t=turtle.Turtle()

t.speed(3)
t.color("red")

for _ in range(3):
    t.forward(100)
    t.left(120)

turtle.done()



# circle programm
import turtle
t=turtle.Turtle()
t.circle(100)
turtle.done()




# star programm
import turtle
t=turtle.Turtle()

for _ in range(5):
    t.forward(100)
    t.right(144)
turtle.done()







