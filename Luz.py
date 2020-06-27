from turtle import *

class Luz:

	color = "#3F3F3F"
	rayo = ""
	x = 0.0
	y = 0.0
	primerRebote = True

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.rayo = Turtle()
		self.rayo.ht()
		self.rayo.speed(0)
		self.rayo.pensize(2)
		self.rayo.setundobuffer(None)

	#Mueve el rayo de vuelta al origen
	def goHome(self):
		self.rayo.up()
		self.rayo.setpos(self.x, self.y)
		#self.rayo.setheading(360)
		self.rayo.down()

	#Pone la direccion del rayo
	def rotar(self, grados):
		self.rayo.up()
		self.rayo.setheading(grados)
		self.rayo.down()

	#Cambial al color y se mueve un pixel
	def go(self, color):
		self.rayo.pencolor(color)
		self.rayo.forward(1)

	def gof(self):
		self.rayo.forward(1)

	def getX(self):
		return self.rayo.xcor()

	def getY(self):
		return self.rayo.ycor()

	def getDir(self):
		return self.rayo.heading()

	#Retorna el valor de rebote
	def puedeRebotar(self):
		return self.primerRebote

	def setRebote(self, estado):
		self.primerRebote = estado

	#Calcula la rotación según el ángulo y la pared con la que está chocando
	def cambioDireccion(self, orientacion, dir):
		self.rayo.backward(1)

		if(orientacion == 1):	#pared vertical
			#Obtiene el ángulo interno que no conocemos y el ángulo a rotar es el doble de este
			
			if(90 > dir > 0):				#  	\  |
				x = 90 - dir 				#  	 \ |
				angulo = (x*2) 				#  	  \|
				self.rayo.left(angulo) 		#  	  /|
											#	 v |

			elif(180 > dir > 90):			#  |  /
				x = 90 - dir 				#  | /
				angulo = (-x*2) 			#  |/
				self.rayo.right(angulo) 	#  |\
 											#  | v

			elif(270 > dir > 180):			#  | ^ 
				x = 90 - dir 				#  |/  
				angulo = (-x*2) 			#  |\
				self.rayo.right(angulo) 	#  | \
											#  |  \ 

			elif(360 > dir > 270):			#  	^ |
				x = 90 - (360 - dir) 		#  	 \|
				angulo = (x*2) 				#  	 /|
				self.rayo.right(angulo) 	#  	/ |
											#  /  |

		else:					#pared horizontal

			#Siempre es el doble de la direccion actual (rotándolo a donde corresponda)

			if(90 > dir > 0):				#	  \
				angulo = (-dir*2)			#	   \	^
				self.rayo.left(angulo)		#		\  /
											#________\/_________

			elif(180 > dir > 90):			#	  		 /
				angulo = (dir*2)			#	   ^    /
				self.rayo.right(angulo)		#		\  /
											#________\/_________

			elif(270 > dir > 180):			#___________________
				angulo = (dir*2)			#		 /\
				self.rayo.right(angulo)		#		v  \
											#			\

			elif(360 > dir > 270):			#___________________
				angulo = (-dir*2)			#		 /\
				self.rayo.left(angulo)		#		/  v
											#	   /