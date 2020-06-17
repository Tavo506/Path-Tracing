from turtle import *
import numpy as np 
import random as r
from PIL import Image
from Luz import *
import threading



def pathtracing(Rayo):
    
    for veces in range(360):

        Rayo.goHome()
        dir = r.randint(1, 360)
        Rayo.rotar(dir)
        Rayo.go()



im_file = Image.open("fondo.png")
ref = np.array(im_file)

title("Path Tracing 4K")
setup(500, 500)

Rayo1 = Luz(180, 305)
Rayo1.goHome()


#thread setup
t = threading.Thread(target = pathtracing, args=(Rayo1,)) # f being the function that tells how the ball should move
t.setDaemon(True) # Alternatively, you can use "t.daemon = True"
t.start()

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
