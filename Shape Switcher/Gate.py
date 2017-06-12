from OpenGL.GL import *
from OpenGL.GLUT import *
from Global import *

class GATE:
		def __init__(self, index, shape = None, color = None, direction = "v"):
			self.index = index 				# position
			self.shapeType = shape 			# shape to be set
			self.color = color 				# color to be set
			self.direction = direction 		# Gate direction
			self.opening = False 			# indicates that the gate is opening		
			self.inc = 0 					# for opening animation
			self.opened = False 			# indicates that the gate is opened
			d[self.index] = "gate" 			# add Gate to dictionary

		def setIndex(self, index):
			self.index = index

		def getIndex(self):
			return self.index

		def getDirection(self): 			# returns Gate direction ("v" or "h")
			return self.direction

		def draw(self):
			glMatrixMode(GL_MODELVIEW)
			glLoadIdentity()
			glTranslate(indexDec(self.index)[0], indexDec(self.index)[1], 0)

			if self.shapeType == None: 		# Gate has only color
				if self.color == "red":		# Gate color is red
					if self.direction == "v":	# Gate is vertical
						# draw a vertical Gate
						glColor(1, 50 / 255, 50 / 255)
						# top half
						glBegin(GL_POLYGON)
						glVertex(0.3, 1.02, 0.5)
						glVertex(0.4, 1.2, 0.5)
						glVertex(0.4, 0.5 + self.inc, 0.5)
						glVertex(0.3, 0.5 + self.inc, 0.5)
						glEnd()

						glColor(254 / 255, 69 / 255, 69 / 255)
						glBegin(GL_POLYGON)
						glVertex(0.4, 1.2, 0.5)
						glVertex(0.6, 1.2, 0.5)
						glVertex(0.6, 0.5 + self.inc, 0.5)
						glVertex(0.4, 0.5 + self.inc, 0.5)
						glEnd()
						
						glColor(1, 50 / 255, 50 / 255)
						# bottom half
						glBegin(GL_POLYGON)
						glVertex(0.3, -0.01, 0.5)
						glVertex(0.4, -0.1, 0.5)
						glVertex(0.4, 0.5 - self.inc, 0.5)
						glVertex(0.3, 0.5 - self.inc, 0.5)
						glEnd()
						glColor(254 / 255, 69 / 255, 69 / 255)
						glBegin(GL_POLYGON)
						glVertex(0.4, -0.1, 0.5)
						glVertex(0.6, -0.1, 0.5)
						glVertex(0.6, 0.5 - self.inc, 0.5)
						glVertex(0.4, 0.5 - self.inc, 0.5)
						glEnd()

					else: 					# Gate is horizontal
						glColor(1, 50 / 255, 50 / 255)
						glBegin(GL_POLYGON)
						glVertex(-0.2, 0.4, 0.5)
						glVertex(-0.2, 0.6, 0.5)
						glVertex(0.5 - self.inc, 0.6, 0.5)
						glVertex(0.5 - self.inc, 0.4, 0.5)
						glEnd()
						glBegin(GL_POLYGON)
						glVertex(0.5 + self.inc, 0.6, 0.5)
						glVertex(1.2, 0.6, 0.5)
						glVertex(1.2, 0.4, 0.5)
						glVertex(0.5 + self.inc, 0.4, 0.5)
						glEnd()
						glColor(254 / 255, 69 / 255, 69 / 255)
						glBegin(GL_POLYGON)
						glVertex(-0.02, 0.3, 0.5)
						glVertex(-0.2, 0.4, 0.5)
						glVertex(0.5 - self.inc, 0.4, 0.5)
						glVertex(0.5 - self.inc, 0.3, 0.5)
						glEnd()
						glBegin(GL_POLYGON)
						glVertex(0.5 + self.inc, 0.4, 0.5)
						glVertex(1.2, 0.4, 0.5)
						glVertex(1.02, 0.3, 0.5)
						glVertex(0.5 + self.inc, 0.3, 0.5)
						glEnd()

				elif self.color == "green": 		# Gate color is green
					if self.direction == "v":
						glColor(0.2, 0.9, 0.2)
						glBegin(GL_POLYGON)
						glVertex(0.3, 1.02, 0.5)
						glVertex(0.4, 1.2, 0.5)
						glVertex(0.4, 0.5 + self.inc, 0.5)
						glVertex(0.3, 0.5 + self.inc, 0.5)
						glEnd()
						glColor(0, 228 / 255, 0)
						glBegin(GL_POLYGON)
						glVertex(0.4, 1.2, 0.5)
						glVertex(0.6, 1.2, 0.5)
						glVertex(0.6, 0.5 + self.inc, 0.5)
						glVertex(0.4, 0.5 + self.inc, 0.5)
						glEnd()
						glColor(0.2, 0.9, 0.2)
						glBegin(GL_POLYGON)
						glVertex(0.3, -0.01, 0.5)
						glVertex(0.4, -0.1, 0.5)
						glVertex(0.4, 0.5 - self.inc, 0.5)
						glVertex(0.3, 0.5 - self.inc, 0.5)
						glEnd()
						glColor(0, 228 / 255, 0)
						glBegin(GL_POLYGON)
						glVertex(0.4, -0.1, 0.5)
						glVertex(0.6, -0.1, 0.5)
						glVertex(0.6, 0.5 - self.inc, 0.5)
						glVertex(0.4, 0.5 - self.inc, 0.5)
						glEnd()

					else:
						glColor(0, 228 / 255, 0)
						glBegin(GL_POLYGON)
						glVertex(-0.2, 0.4, 0.5)	
						glVertex(-0.2, 0.6, 0.5)
						glVertex(0.5 - self.inc, 0.6, 0.5)
						glVertex(0.5 - self.inc, 0.4, 0.5)
						glEnd()
						glBegin(GL_POLYGON)
						glVertex(0.5 + self.inc, 0.6, 0.5)
						glVertex(1.2, 0.6, 0.5)
						glVertex(1.2, 0.4, 0.5)
						glVertex(0.5 + self.inc, 0.4, 0.5)
						glEnd()
						glColor(0.2, 0.9, 0.2)
						glBegin(GL_POLYGON)
						glVertex(-0.02, 0.3, 0.5)
						glVertex(-0.2, 0.4, 0.5)
						glVertex(0.5 - self.inc, 0.4, 0.5)
						glVertex(0.5 - self.inc, 0.3, 0.5)
						glEnd()
						glBegin(GL_POLYGON)
						glVertex(0.5 + self.inc, 0.4, 0.5)
						glVertex(1.2, 0.4, 0.5)
						glVertex(1.02, 0.3, 0.5)
						glVertex(0.5 + self.inc, 0.3, 0.5)
						glEnd()

				elif self.color == "blue":		# Gate color is blue
					if self.direction == "v":
						glColor(0, 200 / 255, 1)
						glBegin(GL_POLYGON)
						glVertex(0.3, 1.02, 0.5)
						glVertex(0.4, 1.2, 0.5)
						glVertex(0.4, 0.5 + self.inc, 0.5)
						glVertex(0.3, 0.5 + self.inc, 0.5)
						glEnd()
						glColor(0, 153 / 255, 1)
						glBegin(GL_POLYGON)
						glVertex(0.4, 1.2, 0.5)
						glVertex(0.6, 1.2, 0.5)
						glVertex(0.6, 0.5 + self.inc, 0.5)
						glVertex(0.4, 0.5 + self.inc, 0.5)
						glEnd()
						glColor(0, 200 / 255, 1)
						glBegin(GL_POLYGON)
						glVertex(0.3, -0.01, 0.5)
						glVertex(0.4, -0.1, 0.5)
						glVertex(0.4, 0.5 - self.inc, 0.5)
						glVertex(0.3, 0.5 - self.inc, 0.5)
						glEnd()
						glColor(0, 153 / 255, 1)
						glBegin(GL_POLYGON)
						glVertex(0.4, -0.1, 0.5)
						glVertex(0.6, -0.1, 0.5)
						glVertex(0.6, 0.5 - self.inc, 0.5)
						glVertex(0.4, 0.5 - self.inc, 0.5)
						glEnd()

					else:
						glColor(0, 153 / 255, 1)
						glBegin(GL_POLYGON)
						glVertex(-0.2, 0.4, 0.5)
						glVertex(-0.2, 0.6, 0.5)
						glVertex(0.5 - self.inc, 0.6, 0.5)
						glVertex(0.5 - self.inc, 0.4, 0.5)
						glEnd()
						glBegin(GL_POLYGON)
						glVertex(0.5 + self.inc, 0.6, 0.5)
						glVertex(1.2, 0.6, 0.5)
						glVertex(1.2, 0.4, 0.5)
						glVertex(0.5 + self.inc, 0.4, 0.5)
						glEnd()
						glColor(0, 200 / 255, 1)
						glBegin(GL_POLYGON)
						glVertex(-0.02, 0.3, 0.5)
						glVertex(-0.2, 0.4, 0.5)
						glVertex(0.5 - self.inc, 0.4, 0.5)
						glVertex(0.5 - self.inc, 0.3, 0.5)
						glEnd()
						glBegin(GL_POLYGON)
						glVertex(0.5 + self.inc, 0.4, 0.5)
						glVertex(1.2, 0.4, 0.5)
						glVertex(1.02, 0.3, 0.5)
						glVertex(0.5 + self.inc, 0.3, 0.5)
						glEnd()
			# gate has shape on it
			else:						# draw a blank gate
				if self.direction == "v":
					glColor(0.5, 0.5, 0.5)
					glBegin(GL_POLYGON)
					glVertex(0.3, 1.02, 0.5)
					glVertex(0.4, 1.2, 0.5)
					glVertex(0.4, 0.5 + self.inc, 0.5)
					glVertex(0.3, 0.5 + self.inc, 0.5)
					glEnd()
					glColor(0.6, 0.6, 0.6)
					glBegin(GL_POLYGON)
					glVertex(0.4, 1.2, 0.5)
					glVertex(0.6, 1.2, 0.5)
					glVertex(0.6, 0.5 + self.inc, 0.5)
					glVertex(0.4, 0.5 + self.inc, 0.5)
					glEnd()
					glColor(0.5, 0.5, 0.5)
					glBegin(GL_POLYGON)
					glVertex(0.3, -0.01, 0.5)
					glVertex(0.4, -0.1, 0.5)
					glVertex(0.4, 0.5 - self.inc, 0.5)
					glVertex(0.3, 0.5 - self.inc, 0.5)
					glEnd()
					glColor(0.6, 0.6, 0.6)
					glBegin(GL_POLYGON)
					glVertex(0.4, -0.1, 0.5)
					glVertex(0.6, -0.1, 0.5)
					glVertex(0.6, 0.5 - self.inc, 0.5)
					glVertex(0.4, 0.5 - self.inc, 0.5)
					glEnd()

				else:
					glColor(0.6, 0.6, 0.6)
					glBegin(GL_POLYGON)
					glVertex(-0.2,0.4,0.5)
					glVertex(-0.2,0.6,0.5)
					glVertex(0.5 - self.inc,0.6,0.5)
					glVertex(0.5 - self.inc,0.4,0.5)
					glEnd()
					glBegin(GL_POLYGON)
					glVertex(0.5 + self.inc,0.6,0.5)
					glVertex(1.2,0.6,0.5)
					glVertex(1.2,0.4,0.5)
					glVertex(0.5 + self.inc,0.4,0.5)
					glEnd()
					glColor(0.5, 0.5, 0.5)
					glBegin(GL_POLYGON)
					glVertex(-0.02,0.3,0.5)
					glVertex(-0.2,0.4,0.5)
					glVertex(0.5 - self.inc,0.4,0.5)
					glVertex(0.5 - self.inc,0.3,0.5)
					glEnd()
					glBegin(GL_POLYGON)
					glVertex(0.5 + self.inc,0.4,0.5)
					glVertex(1.2,0.4,0.5)
					glVertex(1.02,0.3,0.5)
					glVertex(0.5 + self.inc,0.3,0.5)
					glEnd()

		def setShape(self):			# draw shape on the Gate
			glMatrixMode(GL_MODELVIEW)
			glLoadIdentity()
			glTranslate(indexDec(self.index)[0], indexDec(self.index)[1], 0)

			if self.color == "red":		# set shape color
				glColor(1, 50 / 255, 50 / 255)
			elif self.color == "green":
				glColor(0, 228 / 255, 0)
			elif self.color == "blue":
				glColor(0 ,153 / 255, 1)
			else:
				glColor(0.9, 0.9, 0.9)

			if self.shapeType == "rect":
				if self.opening:		# draw nothing while opening the Gate
					pass
				else:
					glTranslate(0.5, 0.5, 0.9)		# to draw at center (0.5, 0.5)
					glutSolidCube(0.24)
					# border
					glColor(0.4, 0.4, 0.4)
					glutWireCube(0.24)

			elif self.shapeType == "circle":
				if self.opening:		# draw nothing while opening the Gate
					pass
				else:
					glTranslate(0.5, 0.5, 0.9)
					glutSolidSphere(0.14, 20, 2)	# to draw at center (0.5, 0.5)

			elif self.shapeType == "tri":
				if self.opening == True:	# draw nothing while opening the Gate
					pass
				else:
					glBegin(GL_POLYGON)
					glVertex(0.4, 0.62, 0.9)
					glVertex(0.4, 0.38, 0.9)
					glVertex(0.62, 0.5, 0.9)
					glEnd()
					# border
					glColor(0.4, 0.4, 0.4)
					glBegin(GL_LINE_LOOP)
					glVertex(0.4, 0.62, 0.9)
					glVertex(0.4, 0.38, 0.9)
					glVertex(0.62, 0.5, 0.9)
					glEnd()

		def getShape(self): 		# returns shape drawn on the Gate
			return self.shapeType

		def getColor(self):			# returns Gate color
			return self.color

		def open(self):					# opens the Gate
			self.opening = True			# the Gate is now opening
			if not self.opened:			# if the Gate is not opened (closed)
				self.inc += 0.15
			if self.inc >= 0.43:		# opning limit
				self.opened = True		# Gate is now opened

		def close(self):
			self.opening = False		# Gate is not opening --> allowed to draw shapes
			if self.opened:				# check if the Gate is opened first
				self.inc -= 0.15		# for closing
			if self.inc <= 0:			# back to normal 
				self.inc = 0
				self.opened = False		# Gate is now closed