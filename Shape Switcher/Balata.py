from OpenGL.GL import *
from OpenGL.GLUT import *
from Global import *

class BALATA:
	def __init__(self):
		self.index = "" 			# initialize position
		self.shapeType = None		# initialize shape drawn to None
		self.color = None			# initialize color drawn to None

	def setIndex(self, index):
		self.index = index
		# d[self.index] = "balata"

	def getIndex(self):
		return self.index

	def draw(self, index):
		self.index = index
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glColor(1, 1, 0.8)		# almost white
		glTranslate(indexDec(self.index)[0], indexDec(self.index)[1], 0)	# translate to required position
		# draw Balata polygon
		glBegin(GL_POLYGON)		
		glVertex(0, 0, -0.9)
		glVertex(1, 0, -0.9)
		glVertex(1, 1, -0.9)
		glVertex(0, 1, -0.9)
		glEnd()
		# border
		glColor(0.6, 0.6, 0.6)
		glBegin(GL_LINE_LOOP)
		glVertex(0,0, -0.5)
		glVertex(1,0, -0.5)
		glVertex(1,1, -0.5)
		glVertex(0,1, -0.5)
		glEnd()

	def drawWall(self, index):		# draw a Wall at "index" position
		self.index = index
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glColor(0.5, 0.5, 0.5)
		glTranslate(indexDec(self.index)[0] , indexDec(self.index)[1], 0)
		glBegin(GL_POLYGON)
		glVertex(0,0,-0.9)
		glVertex(1,0,-0.9)
		glVertex(1,1,-0.9)
		glVertex(0,1,-0.9)
		glEnd()

		glColor(.4,.4,.4)
		glBegin(GL_POLYGON)
		glVertex(.2,.2,-0.1)
		glVertex(.8,.2,-0.1)
		glVertex(.8,.9,-0.1)
		glVertex(.2,.9,-0.1)
		glEnd()

		glBegin(GL_LINES)
		glVertex(0,0,-0.5)
		glVertex(0,1,-0.5)
		glVertex(1,0,-0.5)
		glVertex(1,1,-0.5)
		glVertex(.2,.2,-0.5)
		glVertex(0,0,-0.5)
		glVertex(.8,.2,-0.5)
		glVertex(1,0,-0.5)
		glVertex(.2,.9,-0.5)
		glVertex(0,1,-0.5)
		glVertex(.8,.9,-0.5)
		glVertex(1,1,-0.5)
		glVertex(0,0,-0.5)
		glVertex(1,0,-0.5)
		glVertex(1,1,-0.5)
		glVertex(0,1,-0.5)
		glEnd()

	def setShape(self, index, type1):	# draw a shape on Balata
		self.shapeType = type1
		self.index = index

		glLoadIdentity()
		glColor(0.72, 0.72, 0.72)		# grey
		if self.shapeType == "circle":
			glTranslate(indexDec(self.index)[0] + 0.5, indexDec(self.index)[1] + 0.5, 0)
			glutSolidSphere(0.33, 20, 2)
		elif self.shapeType == "rect":
			glTranslate(indexDec(self.index)[0] + 0.5, indexDec(self.index)[1] + 0.5, 0)
			glutSolidCube(0.66)
		elif self.shapeType == "tri":
			glTranslate(indexDec(self.index)[0], indexDec(self.index)[1], 0)
			glBegin(GL_POLYGON)
			glVertex2d(0.2, 0.2)
			glVertex2d(0.8, 0.2)
			glVertex2d(0.5, 0.8)
			glEnd()
		elif self.shapeType == "star":
			glTranslate(indexDec(self.index)[0], indexDec(self.index)[1], 0)
			glColor(1, 228 / 255, 53 / 255)
			glBegin(GL_POLYGON)
			glVertex2d(0.5, 0.8)
			glVertex2d(0.7, 0.2)
			glVertex2d(0.5, 0.35)
			glVertex2d(0.3, 0.2)
			glEnd()
			glBegin(GL_POLYGON)
			glVertex2d(0.2, 0.6)
			glVertex2d(0.8, 0.6)
			glVertex2d(0.5, 0.35)
			glEnd()

	def getShape(self):			# return shape drawn on Balta
		return self.shapeType

	def setColor(self, index):	# draw a color on Balata
		self.index = index
		glMatrixMode (GL_MODELVIEW)
		glLoadIdentity()
		glColor(1, 1, 0.8)
		glTranslate(indexDec(self.index)[0] , indexDec(self.index)[1], 0)

		# textures used
		glBegin(GL_POLYGON)
		glTexCoord(-0.05, -0.05)
		glVertex(0, 0, 0)
		glTexCoord(-0.05, 1.05)
		glVertex(0, 1, 0)
		glTexCoord(1.05, 1.05)
		glVertex(1, 1, 0)
		glTexCoord(1.05, -0.05)
		glVertex(1, 0, 0)
		glEnd()

		glTranslate(0, 0, 0.1)
		glColor(0.6, 0.6, 0.6)
		glBegin(GL_LINE_LOOP)
		glVertex(0, 0, 0)
		glVertex(0, 1, 0)
		glVertex(1, 1, 0)
		glVertex(1, 0, 0)
		glEnd()

	def getColor(self):			# return color of Balata
		return self.color

