from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
from Global import *
from Balata import BALATA
from Gate import GATE
from Zalata import ZALATA
import pygame

setLevel(d2)

def setDict():
	for i in range(9):
		d["0, {}".format(i)] = "wall"

	for i in range(9):
		d["10, {}".format(i)] = "wall"

	for i in range(1, 10):
		d["{}, 0".format(i)] = "wall"

	for i in range(1, 10):
		d["{}, 8".format(i)] = "wall"

b1 = BALATA()

g1 = GATE("3, 3", None, "blue", "h")
g2 = GATE("1, 5", "tri", None, "h")
g3 = GATE("3, 7", "rect", None, "v")
g4 = GATE("4, 1", None, "green", "v")
g5 = GATE("5, 6", None, "red", "v")
g6 = GATE("6, 5", None, "green", "h")
g7 = GATE("6, 2", "tri", None, "v")
g8 = GATE("8, 3", "circle", None, "h")
g9 = GATE("8, 5", "rect", "blue", "h")
gateList = [g1, g2, g3, g4, g5, g6, g7, g8, g9]

s = ZALATA("2, 4", "circle" ,"red")

setDict()

def init( ):
	glClearColor (0.8, 0.8, 0.8, 0.0) # background color
	glEnable(GL_DEPTH_TEST)
	glMatrixMode (GL_PROJECTION)
	glLoadIdentity ()
	# seen coordinates
	glOrtho(0, 11, 0 , 11 , -1 , 1) # l,r,b,t,n,f

	global texture, imgload, img, width, height
	texture = glGenTextures(3)

	imgload = pygame.image.load("images/balata_color_blue.png")
	#imgload = pygame.image.load("sky.bmp")
	img = pygame.image.tostring(imgload, "RGBA", 1)
	width = imgload.get_width()
	height = imgload.get_height()

	# "Bind" the newly created texture : all future texture functions will modify this texture
	glBindTexture(GL_TEXTURE_2D, texture[0])
	glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
	glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA,GL_UNSIGNED_BYTE, img)

	imgload = pygame.image.load("images/balata_color_red.png")
	img = pygame.image.tostring(imgload, "RGBA", 1)
	width = imgload.get_width()
	height = imgload.get_height()
	glBindTexture(GL_TEXTURE_2D, texture[1])
	glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
	glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA,GL_UNSIGNED_BYTE, img)

	imgload = pygame.image.load("images/balata_color_green.png")
	img = pygame.image.tostring(imgload, "RGBA", 1) # try 0)
	width = imgload.get_width()
	height = imgload.get_height()
	glBindTexture(GL_TEXTURE_2D, texture[2])
	glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) # GL_CLAMP)
	glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) # GL_CLAMP)
	glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA,GL_UNSIGNED_BYTE, img)

	glEnable(GL_TEXTURE_2D)


def drawDict():
	glLineWidth(1)
	for i in d:
		if d[i] == "balata":
			b1.draw(i)
		elif d[i] == "balata shape tri":
			b1.draw(i)
			b1.setShape(i, "tri")
		elif d[i] == "balata shape rect":
			b1.draw(i)
			b1.setShape(i, "rect")
		elif d[i] == "balata shape circle":
			b1.draw(i)
			b1.setShape(i, "circle")
		elif d[i] == "balata shape star":
			b1.draw(i)
			b1.setShape(i, "star")
		elif d[i] == "balata color red":
			glBindTexture(GL_TEXTURE_2D, texture[1])
			b1.setColor(i)
		elif d[i] == "balata color green":
			glBindTexture(GL_TEXTURE_2D, texture[2])
			b1.setColor(i)
		elif d[i] == "balata color blue":
			glBindTexture(GL_TEXTURE_2D, texture[0])
			b1.setColor(i)
		elif d[i] == "wall":
			b1.drawWall(i)

def setGate(gate):
	x1 = indexDec(s.getIndex())
	x2 = indexDec(gate.getIndex())
	if gate.getDirection() == "v":
		if gate.getColor() == None:
			b = x1[0] in arange(x2[0] - 1, x2[0] + 1.25, 0.25) \
			and x1[1] in arange(x2[1], x2[1] + 1.25, 0.25) \
			and s.getShape() == gate.getShape()
			return b
		else:
			if gate.getShape() == None:
				b = x1[0] in arange(x2[0] - 1, x2[0] + 1.25, 0.25) \
				and x1[1] in arange(x2[1], x2[1] + 1.25, 0.25) \
				and s.getColor() == gate.getColor()
				return b
			else:
				b = x1[0] in arange(x2[0] - 1, x2[0] + 1.25, 0.25) \
				and x1[1] in arange(x2[1], x2[1] + 1.25, 0.25) \
				and s.getColor() == gate.getColor() \
				and s.getShape() == gate.getShape()
				return b
	else:
		if gate.getColor() == None:
			b = x1[0] in arange(x2[0], x2[0] + 1.25, 0.25) \
			and x1[1] in arange(x2[1] - 1, x2[1] + 1.25, 0.25) \
			and s.getShape() == gate.getShape()
			return b
		else:
			if gate.getShape() == None:
				b = x1[0] in arange(x2[0], x2[0] + 1.25, 0.25) \
				and x1[1] in arange(x2[1] - 1, x2[1] + 1.25, 0.25) \
				and s.getColor() == gate.getColor()
				return b
			else:
				b = x1[0] in arange(x2[0], x2[0] + 1.25, 0.25) \
				and x1[1] in arange(x2[1] - 1, x2[1] + 1.25, 0.25) \
				and s.getColor() == gate.getColor() \
				and s.getShape() == gate.getShape()
				return b

def drawGate(gate):
	b1.draw(gate.getIndex())
	gate.draw()
	gate.setShape()

def openGates():

	if setGate(g1):
		g1.open()
		s.setPassGate(True)

	elif setGate(g2):
		g2.open()
		s.setPassGate(True)

	elif setGate(g3):
		g3.open()
		s.setPassGate(True)

	elif setGate(g4):
		g4.open()
		s.setPassGate(True)

	elif setGate(g5):
		g5.open()
		s.setPassGate(True)

	elif setGate(g6):
		g6.open()
		s.setPassGate(True)

	elif setGate(g7):
		g7.open()
		s.setPassGate(True)

	elif setGate(g8):
		g8.open()
		s.setPassGate(True)

	elif setGate(g9):
		g9.open()
		s.setPassGate(True)

	else:
		g1.close()
		g2.close()
		g3.close()
		g4.close()
		g5.close()
		g6.close()
		g7.close()
		g8.close()
		g9.close()
		s.setPassGate(False)

def writeStrokeText(width, scale, string, x, y, r, g, b):
    glLineWidth(width)
    glColor(r, g, b)  # Yellow Color
    glLoadIdentity()
    glTranslate(x, y, 0)
    glScale(scale, scale, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def writeBitmapText(string, x, y, r, g, b):
    glLoadIdentity()
    glColor3f(r, g, b)
    glScalef(1.04, 1.04, 1);
    glRasterPos3f(x, y, 0);

    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, c)

def writeTextandtimer():
    shape = "SHAPE"
    writeStrokeText(4, 0.0055, shape, 2.5, 10, 1, 1, .1)
    switcher = "SWITCHER"
    writeStrokeText(4, 0.0055, switcher, 5, 10, 1, 0, 0)

    # playsound("bomb.mp3")
    # pygame.mixer.music.load("bomb.mp3")
    # pygame.mixer.music.play()

def draw():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
	drawDict()

	for g in gateList:
		drawGate(g)

	s.draw()

	l = indexDec(s.getIndex())
	x = "{}, {}".format(round(l[0]), round(l[1]))
	if d[x] == "balata shape star":
		t2string =  "BRAVO!.. press space to continue"
		glutKeyboardFunc(keyboard)
	else:
		t2string = "Collect required shapes/colors to cross the gates"
	
	writeStrokeText(1.4, 0.003, t2string, 0.8, 9.3, 0.4, .2, 0.6)

	writeTextandtimer()

	openGates()

	glutSwapBuffers()

def keyboard(key, x, y):
	if key == b' ':
		import Level_3
		glDeleteTextures(texture)

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH )
init()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(s.move)
glutMainLoop()