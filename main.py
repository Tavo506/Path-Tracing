from turtle import *
import numpy as np 
import random
from PIL import Image
from Luz import *
import threading

def getColor(x, y, i, ri, gi, bi):
    i = i // 3      #Calcula la intencidad

    colorRGB = px[int(x),int(y)]    #Obtiene el color en el pixel actual

    R = colorRGB[0]     #Separa los tres colores
    G = colorRGB[1]
    B = colorRGB[2]

    #Crea el número hexadecimal del color actual para luego compararlo con las paredes y cristales
    colorH = "#" + str(hex(R).split('x')[-1]) + str(hex(G).split('x')[-1]) + str(hex(B).split('x')[-1])

    #Realiza los ajustes del color con intencidad y tono
    R = R - i + ri
    G = G - i + gi
    B = B - i + bi

    #Calcula cada color en hexadecimal tomando los casos posibles

    if(R >= 16):            #Si es mayor a 15 queda igual
        R = hex(R).split('x')[-1]
    elif(R >= 0):           #Si es menor coloca un 0 al frente y concatena
        R = "0" + hex(R).split('x')[-1]
    else:                   #Si es un número negativo entonces debe ser cero
        R = "00"

    if(G >= 16):
         G = hex(G).split('x')[-1]
    elif(G >= 0):
        G = "0" + hex(G).split('x')[-1]
    else:
        G = "00"

    if(B  >= 16):
        B = hex(B).split('x')[-1]
    elif(B >= 0):
        B = "0" + hex(B).split('x')[-1]
    else:
        B = "00"

    colorRGB = "#" + R + G + B      #Concatena los colores como un color hexadecimal

    return [colorH, colorRGB]

#Pregunta si 4 pixeles arriba del actual sigue siendo pared, de ser así quiere decir que es una pared vertical
def calcularDireccion(x, y):
    color = getColor(x, y+4, 0, 0, 0, 0)
    if(color[0] in ["#d7d4cf", "#812b2b", "#6d6d6d"]): #Paredes
        return 1    #vertical
    else:
        return 2    #horizontal

#def getOpcionPared()

def pathtracing(Rayo, direcciones, rl, gl, bl):
    
    for veces in range(100):

        Rayo.goHome()   #Va al origen

        Rayo.setRebote(True)

        try:
            dir = random.choice(direcciones) #Obtiene un ángulo
            direcciones.pop(direcciones.index(dir)) #Elimina el ángulo de la lista
        except:
            return

        Rayo.rotar(dir) #Rota el rayo a la dirección
        color = ["",""]

        ri = rl     #Vuelve a setear los colores al de la fuente de luz
        gi = gl
        bi = bl

        for i in range(255):    #"i" es el alcance

            
            #Recupera las coordenadas actuales
            x = Rayo.getX()
            y = Rayo.getY()

            if(500 < x or x < 0 or 500 < y or y < 0):   #Si se sale de la pantalla se detiene
                break

            try:
                color = getColor(x, y, i, ri, gi, bi)  #Obtiene el color en las coordenadas actuales para pintar
            except:
                update()

            if(color[1] == "#000000"):  #Si el color es negro deja de calcular más
                break

            Rayo.go(color[1])  #Se mueve uno y pinta

            if(color[0] in ["#d7d4cf", "#6d6d6d"]): #Si el color es un muro:
                if(Rayo.puedeRebotar()):    #Si aún no rebota...
                    Rayo.setRebote(False)   #Pone que ya rebotó
                    orientacion = calcularDireccion(x, y)   #Calcula si la pared es vertical u horizontal
                    Rayo.cambioDireccion(orientacion, dir)  #Calcula la rotación
                    Rayo.go(color[1])
                else:
                    break

            elif(color[0] == "#ec7ca1"):    #Cristal rosado
                ri = 20                     #Lo tiñe de rosa
                gi = -10
                bi = -10
            elif(color[0]=="#5ad6d0"):      #Cristal celeste
            	ri=-10                      #Lo tiñe de celeste
            	gi=-10
            	bi=20

            elif(color[0] in ["#812b2b"]):  #Pared roja
                if(Rayo.puedeRebotar()):
                    Rayo.setRebote(False)
                    orientacion = calcularDireccion(x, y)
                    Rayo.cambioDireccion(orientacion, dir)
                    Rayo.go(color[1])

                                        #Lo tiñe de rojo y rebota
                    ri = 30
                    gi = -10
                    bi = -10
                else:
                    break

#Crea una lista con las direcciones y crea copias
direcciones = []
for i in range(360):
    direcciones.append(i)

direcciones1 = direcciones[:]
direcciones2 = direcciones[:]
direcciones3 = direcciones[:]
direcciones4 = direcciones[:]
direcciones5 = direcciones[:]
direcciones6 = direcciones[:]

#Carga la imagen y guarda los pixeles en un array
im_file = Image.open("fondo.png")
px = im_file.load()

title("Path Tracing 4K")
setup(500, 500)
bgcolor(0,0,0)
setworldcoordinates(0, 500, 500, 0)
tracer(0,10000) #velocidad de ejecución y actualización de la pantalla

#Crea los rayos de luz para cada fuente
Rayo1 = Luz(180, 305)
Rayo2 = Luz(180, 305)

Rayo3 = Luz(439, 247)

Rayo4 = Luz(170, 37)

Rayo5 = Luz(448, 51)
Rayo6 = Luz(448, 51)

Rayo7 = Luz(42, 429)

Rayo8 = Luz(153,154)

#thread setup
                                                # La luz, lista dir, tono de luz
t1 = threading.Thread(target = pathtracing, args=(Rayo1,direcciones1,5,5,-5,))
t1.start()

t2 = threading.Thread(target = pathtracing, args=(Rayo2,direcciones1,5,5,-5,))
t2.start()

t3 = threading.Thread(target = pathtracing, args=(Rayo3,direcciones2,5,5,-5,))
t3.start()

t4 = threading.Thread(target = pathtracing, args=(Rayo4,direcciones3,5,5,-5,))
t4.start()

t5 = threading.Thread(target = pathtracing, args=(Rayo5,direcciones4,5,5,-5,))
t5.start()

t6 = threading.Thread(target = pathtracing, args=(Rayo6,direcciones4,5,5,-5,))
t6.start()

t7 = threading.Thread(target = pathtracing, args=(Rayo7,direcciones5,0,-10,-10,))
t7.start()

t8 = threading.Thread(target = pathtracing, args=(Rayo8,direcciones6,5,5,-5,))
t8.start()

done()
