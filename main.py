from turtle import *
import numpy as np 
import random
from PIL import Image
from Luz import *
import threading



def pathtracing(Rayo):
    
    for veces in range(360):

        Rayo.goHome()
        dir = random.randint(1, 360)
        Rayo.rotar(dir)
        for i in range(100):
            x = Rayo.getX()
            y = Rayo.getY()
            if(500 < x or x < 0 or 500 < y or y < 0):
                break
            color = px[int(x),int(y)]
            color = "#" + str(hex(color[0]).split('x')[-1]) + str(hex(color[1]).split('x')[-1]) + str(hex(color[2]).split('x')[-1])
            Rayo.go(color)



im_file = Image.open("fondo.png")
px = im_file.load()

title("Path Tracing 4K")
setup(500, 500)

Rayo1 = Luz(180, 305)
Rayo2 = Luz(180, 305)


#thread setup
t = threading.Thread(target = pathtracing, args=(Rayo1,)) # f being the function that tells how the ball should move
t.setDaemon(True) # Alternatively, you can use "t.daemon = True"
t.start()

k = threading.Thread(target = pathtracing, args=(Rayo2,)) # f being the function that tells how the ball should move
k.setDaemon(True) # Alternatively, you can use "t.daemon = True"
k.start()

"""
t1 = Turtle()
t1.up()
t1.setpos(fix(180), fix(305))
t1.down()

t2 = Turtle()
t2.up()
t2.setpos(fix(152), fix(155))
t2.down()

t3 = Turtle()
t3.up()
t3.setpos(fix(439), fix(247))
t3.down()

t4 = Turtle()
t4.up()
t4.setpos(fix(450), fix(450))
t4.down()
"""

done()
