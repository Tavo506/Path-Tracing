from turtle import *
import numpy as np 
import random
from PIL import Image
from Luz import *
import threading

def getColor(x, y):
    color = px[int(x),int(y)]
    color = "#" + str(hex(color[0]).split('x')[-1]) + str(hex(color[1]).split('x')[-1]) + str(hex(color[2]).split('x')[-1])
    return color


def calcularDireccion(x, y):
    color = getColor(x, y+4)
    if(color in ["#d7d4cf", "#812b2b", "#6d6d6d"]):
        return 1    #vertical
    else:
        return 2    #horizontal

def pathtracing(Rayo, direcciones):
    
    for veces in range(360):

        Rayo.goHome()   #Va al origen

        Rayo.setRebote(True)

        dir = random.randint(1, 360) #Obtiene un ángulo

        while(dir in direcciones):  #Si el ángulo ya se usó selecciona otro
            dir = random.randint(1, 360)

        direcciones.append(dir) #Agrega el ángulo a la lista

        Rayo.rotar(dir) #Rota el rayo a la dirección

        for i in range(200):    #"i" es el alcance

            #Recupera las coordenadas actuales
            x = Rayo.getX()
            y = Rayo.getY()

            if(500 < x or x < 0 or 500 < y or y < 0):   #Si se sale de la pantalla se detiene
                break

            color = getColor(x, y)  #Obtiene el color en las coordenadas actuales para pintar
            Rayo.go(color)  #Se mueve uno y pinta

            if(color in ["#d7d4cf", "#812b2b", "#6d6d6d"]): #Si el color es un muro:
                if(Rayo.puedeRebotar()):
                    Rayo.setRebote(False)
                    Rayo.cambioDireccion(calcularDireccion(x, y), dir)
                else:
                    break


#print("#" + str(hex(109).split('x')[-1]) + str(hex(109).split('x')[-1]) + str(hex(109).split('x')[-1]))

direcciones1 = []
direcciones2 = []

im_file = Image.open("fondo.png")
px = im_file.load()

title("Path Tracing 4K")
setup(500, 500)
bgcolor(0,0,0)
setworldcoordinates(0, 500, 500, 0)

Rayo1 = Luz(180, 305)
Rayo2 = Luz(180, 305)

Rayo3 = Luz(439, 247)
Rayo4 = Luz(439, 247)


#thread setup
t1 = threading.Thread(target = pathtracing, args=(Rayo1,direcciones1,)) # f being the function that tells how the ball should move
t1.setDaemon(True) # Alternatively, you can use "t.daemon = True"
t1.start()

t2 = threading.Thread(target = pathtracing, args=(Rayo2,direcciones1,)) # f being the function that tells how the ball should move
t2.setDaemon(True) # Alternatively, you can use "t.daemon = True"
t2.start()

t3 = threading.Thread(target = pathtracing, args=(Rayo3,direcciones2,)) # f being the function that tells how the ball should move
t3.setDaemon(True) # Alternatively, you can use "t.daemon = True"
t3.start()

t4 = threading.Thread(target = pathtracing, args=(Rayo4,direcciones2,)) # f being the function that tells how the ball should move
t4.setDaemon(True) # Alternatively, you can use "t.daemon = True"
t4.start()


done()
