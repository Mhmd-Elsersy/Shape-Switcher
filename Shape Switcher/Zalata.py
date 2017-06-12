from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
from Global import *

class ZALATA:
	def __init__(self, index, shape, color):
		self.shapeType = shape 				# Zalata shape
		self.color = color 					# Zalata color
		self.index = index 					# Zalata position
		self.passGate = False				# to allow Zalata to cross gates
		self.scale = 1 						# for animation
		self.inc = 0 						
		self.incX = 0
		self.incY = 0
		self.dir = 0 						# direction of movement
		self.leftW = 0
		self.rightW = 0
		self.jump = 0
		self.can_jump = 1

	def setPassGate(self, cond):			# allow/disallow passing gates
		self.passGate = cond
	
	def setIndex(self, index):
		self.index = index
		# d[self.index] = "zalata"

	def getIndex(self):
		return self.index

	def drawEyes(self):						# draw eye circles
		glLoadIdentity()
		glColor(1, 1, 1)
		glTranslate(indexDec(self.index)[0] , indexDec(self.index)[1] + self.jump , 0)
		glTranslate(0.5 + 0.14, 0.5 + 0.14, 0.8)
		glScale(1 + 5 * self.rightW, 1.2 + 5 * self.rightW, 1)
		glutSolidSphere(0.14, 20, 20)

		glLoadIdentity()
		glColor(1, 1, 1)
		glTranslate(indexDec(self.index)[0], indexDec(self.index)[1] + self.jump, 0)
		glTranslate(0.5 - 0.14, 0.5 + 0.14, 0.8)
		glScale(1 + 5 * self.leftW, 1.2 + 5 * self.leftW, 1)
		glutSolidSphere(0.14, 20, 20)

		glLoadIdentity()
		glTranslate(indexDec(self.index)[0], indexDec(self.index)[1] + self.jump, 0)
		glTranslate(0.5 , 0.5 , 0)
		glBegin(GL_LINE_LOOP)
		for i in range(0, 361): # black
			glColor(0, 0, 0)
			x = (0.14 + self.leftW) * math.cos(2*math.pi*i/180) - 0.14
			y = (0.16 + self.leftW) * math.sin(2*math.pi*i/180) + 0.14
			glVertex(x , y, 0.98)
		glEnd()

		glLoadIdentity()
		glTranslate(indexDec(self.index)[0], indexDec(self.index)[1] + self.jump, 0)
		glTranslate(0.5, 0.5, 0)
		glBegin(GL_LINE_LOOP)
		for i in range(0, 361): 
			glColor(0, 0, 0)
			x = (0.14 +  self.rightW) * math.cos(2*math.pi*i/180) + 0.14
			y = (0.16 + self.rightW) * math.sin(2*math.pi*i/180) + 0.14
			glVertex(x , y, 0.95)
		glEnd()

		glLoadIdentity()
		glColor(0, 0, 0)
		glTranslate(indexDec(self.index)[0], indexDec(self.index)[1] + self.jump, 1)
		glTranslate(0.5 - 0.14 + self.incX, 0.5 + 0.14 + self.incY, 0)
		glutSolidSphere(0.05, 20, 2)

		glLoadIdentity()
		glColor(0, 0, 0)
		glTranslate(indexDec(self.index)[0], indexDec(self.index)[1] + self.jump, 1)
		glTranslate(0.5 + 0.14 + self.incX, 0.5 + 0.14 + self.incY, 0)
		glutSolidSphere(0.05, 20, 2)

	def draw(self):		# draw Zalata shape

		glLoadIdentity()
		glTranslate(indexDec(self.index)[0], indexDec(self.index)[1] + self.jump, 0)

		self.setColor()


		if self.shapeType == "circle":
			glTranslate(0.5, 0.5, 0.2)  

			glScale(self.scale, self.scale, 1)   # as it breathing

			if self.scale > 1.06:
				self.inc = 0
			elif self.scale < 1:
				self.inc = 1

			if self.inc:
				self.scale += 0.002
			else:
				self.scale -= 0.002

			glutSolidSphere(0.4, 20, 20)

			self.drawEyes()							# draw Zalata eyes

		elif self.shapeType == "rect":

			glScale(self.scale, self.scale, 1)

			if self.scale > 1.06:
				self.inc = 0
			elif self.scale < 1:
				self.inc = 1

			if self.inc:
				self.scale += 0.0015
			else:
				self.scale -= 0.0015


			if self.dir == 1:				# changing shadow direction according to movement

				glBegin(GL_POLYGON)
				glVertex(0.2,0.1,0.5)
				glVertex(0.8,0.1,0.5)
				glVertex(0.8,0.8,0.5)
				glVertex(0.2,0.8,0.5)
				glEnd()

				glBegin(GL_POLYGON)
				if self.color == "red":
					glColor(0.6, 0, 0)
				elif self.color == "blue":
					glColor(0, 0, 0.6)
				else:
					glColor(0,0.6,0)
				glVertex(0.8,0.8,0.5)
				glVertex(0.7,0.9,0.5)
				glVertex(0.1,0.9,0.5)
				glVertex(0.2,0.8,0.5)
				glEnd()

				glBegin(GL_POLYGON)
				glVertex(0.2,0.8,0.5)
				glVertex(0.2,0.1,0.5)
				glVertex(0.1,0.2,0.5)
				glVertex(0.1,0.9,0.5)
				glEnd()
			else:
				glBegin(GL_POLYGON)
				glVertex(0.2,0.1,0.5)
				glVertex(0.8,0.1,0.5)
				glVertex(0.8,0.8,0.5)
				glVertex(0.2,0.8,0.5)
				glEnd()

				glBegin(GL_POLYGON)
				if self.color == "red":
					glColor(0.6, 0, 0)
				elif self.color == "blue":
					glColor(0, 0, 0.6)
				else:
					glColor(0,0.6,0)
				glVertex(0.8,0.8,0.5)
				glVertex(0.9,0.9,0.5)
				glVertex(0.3,0.9,0.5)
				glVertex(0.2,0.8,0.5)
				glEnd()

				glBegin(GL_POLYGON)
				glVertex(0.8,0.8,0.5)
				glVertex(0.8,0.1,0.5)
				glVertex(0.9,0.2,0.5)
				glVertex(0.9,0.9,0.5)
				glEnd()

			self.drawEyes()

		elif self.shapeType == "tri":

			glScale(self.scale, self.scale, 1)

			if self.scale > 1.06:
				self.inc = 0
			elif self.scale < 1:
				self.inc = 1

			if self.inc:
				self.scale += 0.0015
			else:
				self.scale -= 0.0015


			if self.dir == 1:	
				glBegin(GL_POLYGON)
				glVertex(0.5, 0.1, 0.5)
				glVertex(0.2, 0.8, 0.5)
				glVertex(0.8, 0.8, 0.5)
				glEnd()

				glBegin(GL_POLYGON)
				if self.color == "red":
					glColor(0.6, 0, 0)
				elif self.color == "blue":
					glColor(0, 0, 0.6)
				else:
					glColor(0,0.6,0)		
				glVertex(0.2, 0.8, 0.5)
				glVertex(0.8, 0.8, 0.5)
				glVertex(0.7, 0.9, 0.5)
				glVertex(0.05, 0.9, 0.5)
				glEnd()

				glBegin(GL_POLYGON)		
				glVertex(0.5, 0.1, 0.5)
				glVertex(0.2, 0.8, 0.5)
				glVertex(0.05, 0.9, 0.5)
				glVertex(0.35, 0.2, 0.5)
				glEnd()

			elif self.dir == 0:

				glBegin(GL_POLYGON)
				glVertex(0.5, 0.1, 0.5)
				glVertex(0.2, 0.8, 0.5)
				glVertex(0.8, 0.8, 0.5)
				glEnd()

				glBegin(GL_POLYGON)
				if self.color == "red":
					glColor(0.6, 0, 0)
				elif self.color == "blue":
					glColor(0, 0, 0.6)
				else:
					glColor(0,0.6,0)		
				glVertex(0.2, 0.8, 0.5)
				glVertex(0.8, 0.8, 0.5)
				glVertex(0.95, 0.9, 0.5)
				glVertex(0.25, 0.9, 0.5)
				glEnd()

				glBegin(GL_POLYGON)	
				glVertex(0.5, 0.1, 0.5)
				glVertex(0.8, 0.8, 0.5)
				glVertex(0.95, 0.9, 0.5)
				glVertex(0.65, 0.2, 0.5)
				glEnd()

			self.drawEyes()

	def switchShape(self, shape):			# changes Zalata shape
		if self.shapeType != shape:
			self.shapeType = shape
			self.draw()

	def switchColor(self, color):			# changes Zalata color
		if self.color != color:
			self.color = color
			self.draw()

	def getShape(self):						# returns shape drawn
		return self.shapeType

	def setColor(self):						# set Zalara color
		if self.color == "red":
			glColor(1, 50 / 255, 50 / 255)
		elif self.color == "green":
			glColor(0, 228 / 255, 0)
		elif self.color == "blue":
			glColor(0, 153 / 255, 1)
		else:
			glColor(0, 0, 0)

	def getColor(self):						# returns color
		return self.color

	def move(self, key, x, y):				# movement

		l = indexDec(self.index)			# l = [x, y] --> current position of Zalata
		# convert l to integers "x, y" to allow searching in dictionary
		x = "{}, {}".format(round(l[0]), round(l[1]))

		if "balata shape" in d[x]:			# changing shape
			if "rect" in d[x]:
				self.switchShape("rect")
			elif "tri" in d[x]:
				self.switchShape("tri")
			elif "circle" in d[x]:
				self.switchShape("circle")

		if "balata color" in d[x]:			# changing color
			if "red" in d[x]:
				self.switchColor("red")
			elif "green" in d[x]:
				self.switchColor("green")
			elif "blue" in d[x]:
				self.switchColor("blue")

		if key == GLUT_KEY_LEFT:			# left arrow pressed
			self.dir = 0					# change shadow direction
			self.rightW = 0.03
			self.leftW = 0
	
			l = indexDec(self.index)		# l = [x, y]
			x = "{}, {}".format(int(l[0] - 0.25), round(l[1] + 0.1))  # customize movement

			if d[x] != "gate" or self.passGate == True: # do not pass gate until I let you so
				if "wall" not in d[x]:					# walls are not allowed to be passed
					l[0] -= 0.25						# move left by 0.25 on
					self.incY = 0
					
					self.incX -= 0.1
					if self.incX < 0:
						self.incX = -0.05
					

					if self.jump > 0:
						self.can_jump = 0
					if self.jump < 0:
						self.can_jump = 1

					if self.can_jump:
						self.jump += 0.04
					else:
						self.jump -= 0.04
					self.index = indexEnc(l)			# update Zalata's position to current state
					print(self.index)

		if key == GLUT_KEY_RIGHT:
			self.dir = 1
			self.leftW = 0.03
			self.rightW = 0

			l = indexDec(self.index)
			x = "{}, {}".format(int(l[0] + 1), round(l[1] + 0.1))

			if d[x] != "gate" or self.passGate == True:
				if "wall" not in d[x]:
					l[0] += 0.25
					self.incY = 0

					self.incX += 0.1
					if self.incX > 0:
						self.incX = 0.05
					

					if self.jump > 0:
						self.can_jump = 0
					if self.jump < 0:
						self.can_jump = 1

					if self.can_jump:
						self.jump += 0.04
					else:
						self.jump -= 0.04
					self.index = indexEnc(l)
					print(self.index)

		if key == GLUT_KEY_UP:
			self.rightW = 0
			self.leftW = 0
			
			l = indexDec(self.index)
			x = "{}, {}".format(round(l[0] + 0.1), int(l[1] + 1))

			if d[x] != "gate" or self.passGate == True:
				if "wall" not in d[x]:
					l[1] += 0.25
					self.incX = 0
					self.incY = 0
					
					self.index = indexEnc(l)
					print(self.index)

		if key == GLUT_KEY_DOWN:
			self.rightW = 0
			self.leftW = 0

			l = indexDec(self.index)
			x = "{}, {}".format(round(l[0] + 0.1), int(l[1] - 0.25))

			if d[x] != "gate" or self.passGate == True:
				if "wall" not in d[x]:
					l[1] -= 0.25
					self.incX = 0

					self.incY -= 0.1
					if self.incY < 0:
						self.incY = -0.05

					self.index = indexEnc(l)
					print(self.index)
