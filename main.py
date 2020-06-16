from turtle import *

title("Path Tracing")
screensize(550,550)
bgcolor("#000000")

hideturtle()

color("#FFFFFF")
down()

for i in range(100):
    if(i > 50):
        forward(-1)
    else:
        forward(1)

done()