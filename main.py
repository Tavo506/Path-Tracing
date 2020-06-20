from turtle import *
import numpy as np 
import random
from PIL import Image
from Luz import *
import threading

def getColor(x, y, i):
    i = i // 2

    colorRGB = px[int(x),int(y)]

    R = colorRGB[0]
    G = colorRGB[1]
    B = colorRGB[2]

    colorH = "#" + str(hex(R).split('x')[-1]) + str(hex(G).split('x')[-1]) + str(hex(B).split('x')[-1])

    if(R - i >= 16):
        R = hex(R - i).split('x')[-1]
    elif(R - i >= 0):
        R = "0" + hex(R - i).split('x')[-1]
    else:
        R = "00"

    if(G - i >= 16):
         G = hex(G - i).split('x')[-1]
    elif(G - i >= 0):
        G = "0" + hex(G - i).split('x')[-1]
    else:
        G = "00"

    if(B - i >= 16):
        B = hex(B - i).split('x')[-1]
    elif(B - i >= 0):
        B = "0" + hex(B - i).split('x')[-1]
    else:
        B = "00"

    colorRGB = "#" + R + G + B

    return [colorH, colorRGB]


def calcularDireccion(x, y):
    color = getColor(x, y+4, 0)
    if(color[0] in ["#d7d4cf", "#812b2b", "#6d6d6d"]):
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

        for i in range(255):    #"i" es el alcance

            #Recupera las coordenadas actuales
            x = Rayo.getX()
            y = Rayo.getY()

            if(500 < x or x < 0 or 500 < y or y < 0):   #Si se sale de la pantalla se detiene
                break

            try:
                color = getColor(x, y, i)  #Obtiene el color en las coordenadas actuales para pintar
            except:
                continue

            if(color[1] == "#000000"):
                break

            Rayo.go(color[1])  #Se mueve uno y pinta

            if(color[0] in ["#d7d4cf", "#812b2b", "#6d6d6d"]): #Si el color es un muro:
                if(Rayo.puedeRebotar()):
                    Rayo.setRebote(False)
                    orientacion = calcularDireccion(x, y)
                    print(dir, orientacion)
                    Rayo.cambioDireccion(orientacion, dir)
                    Rayo.go(color[1])  #Se mueve uno y pinta
                else:
                    break
        break
        if(veces % 4 == 0):
            update()
        

#print("#" + str(hex(109).split('x')[-1]) + str(hex(109).split('x')[-1]) + str(hex(109).split('x')[-1]))

direcciones1 = []
direcciones2 = []

im_file = Image.open("fondo.png")
px = im_file.load()

title("Path Tracing 4K")
setup(500, 500)
bgcolor(0,0,0)
setworldcoordinates(0, 500, 500, 0)
tracer(0, 0)

Rayo1 = Luz(180, 305)
Rayo2 = Luz(180, 305)

Rayo3 = Luz(439, 247)
Rayo4 = Luz(439, 247)


#thread setup
t1 = threading.Thread(target = pathtracing, args=(Rayo1,direcciones1,)) # f being the function that tells how the ball should move
t1.setDaemon(True) # Alternatively, you can use "t.daemon = True"
t1.start()

"""
t2 = threading.Thread(target = pathtracing, args=(Rayo2,direcciones1,)) # f being the function that tells how the ball should move
t2.setDaemon(True) # Alternatively, you can use "t.daemon = True"
t2.start()

t3 = threading.Thread(target = pathtracing, args=(Rayo3,direcciones2,)) # f being the function that tells how the ball should move
t3.setDaemon(True) # Alternatively, you can use "t.daemon = True"
t3.start()

t4 = threading.Thread(target = pathtracing, args=(Rayo4,direcciones2,)) # f being the function that tells how the ball should move
t4.setDaemon(True) # Alternatively, you can use "t.daemon = True"
t4.start()
"""

done()
