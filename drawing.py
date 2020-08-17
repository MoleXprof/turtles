#import the turtle module
import turtle

#declare variables
t = turtle.Turtle()
u = 100
t.speed(0)

def drawing():
    for i in range(90):
        for i in range (u):
            t.forward(1)
            t.right(1)
        t.right(144)

drawing()
turtle.done()