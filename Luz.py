from turtle import *

class Luz:

	rayo = ""
	x = 0.0
	y = 0.0

	def __init__(self, x, y):
		self.x = x-250
		self.y = y-250
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
		return self.rayo.xcor()+250

	def getY(self):
		return self.rayo.ycor()+250