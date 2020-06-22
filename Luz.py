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

	def goHome(self):
		self.rayo.up()
		self.rayo.setpos(self.x, self.y)
		#self.rayo.setheading(360)
		self.rayo.down()

	def rotar(self, grados):
		self.rayo.up()
		self.rayo.setheading(grados)
		self.rayo.down()

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

	def puedeRebotar(self):
		return self.primerRebote

	def setRebote(self, estado):
		self.primerRebote = estado

	def cambioDireccion(self, orientacion, dir):
		self.rayo.backward(1)
		if(orientacion == 1):	#pared vertical
			
			if(90 > dir > 0):
				x = 90 - dir
				angulo = (x*2)
				self.rayo.left(angulo)

			elif(180 > dir > 90):
				x = 90 - dir
				angulo = (-x*2)
				self.rayo.right(angulo)

			elif(270 > dir > 180):
				x = 90 - dir
				angulo = (-x*2)
				self.rayo.right(angulo)

			elif(360 > dir > 270):
				x = 90 - (360 - dir)
				angulo = (x*2)
				self.rayo.right(angulo)
		else:					#pared horizontal
			if(90 > dir > 0):
				angulo = (-dir*2)
				self.rayo.left(angulo)

			elif(180 > dir > 90):
				angulo = (dir*2)
				self.rayo.right(angulo)

			elif(270 > dir > 180):
				angulo = (dir*2)
				self.rayo.right(angulo)

			elif(360 > dir > 270):
				angulo = (-dir*2)
				self.rayo.left(angulo)