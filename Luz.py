from turtle import *

class Luz:

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
		if(orientacion == 1):	#vertical
			return
		else:					#horizontal
			if(90 > dir > 0):
				angulo = (90 - dir)*2 + 180
				self.rotar(angulo)
