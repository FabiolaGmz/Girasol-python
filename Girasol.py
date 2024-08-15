

from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0,-40)

for i in range(16):
    for j in range(18):
        color('#FFA216'), rt(90)
        circle(150-j*6,90), lt(90)
        circle(150-j*6,90), rt(180)
    circle(40,24)

color('black') 
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
golden_ang = 137.508
phi = golden_ang * (pi / 180)

for i in range(140):
    r = 4 * sqrt(i)
    theta = i * phi
    x = r * cos(theta)
    y = r * sin(theta)
    penup(), goto(x, y)
    setheading(i * golden_ang)
    pendown(), stamp()

def circulo(x, y):
    penup(), goto(x, y), pendown()
    color('black'), fillcolor('#FFA216')
    begin_fill(), circle(3), end_fill()

def escribir_nombre(nombre):
    penup()
    goto(0, -10)
    color('white')
    write(nombre, align="center", font=("Arial", 24, "normal"))

escribir_nombre("")

hideturtle()
done()
