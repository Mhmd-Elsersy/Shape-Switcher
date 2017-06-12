from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
from Global import *
from Balata import BALATA
from Gate import GATE
from Zalata import ZALATA
import pygame

def setDict():
	for i in range(9):
		d["-1, {}".format(i)] = "wall b"

	for i in range(9):
		d["11, {}".format(i)] = "wall b"

	for i in range(11):
		d["{}, 9".format(i)] = "wall"

	for i in range(11):
		d["{}, -1".format(i)] = "wall b"

	for i in range(9):
		if i == 2 or i == 5 or i == 7:
			d["0, {}".format(i)] = "wall"
		elif i == 0:
			d["0, {}".format(i)] = "balata shape tri"
		elif i == 6:
			d["0, {}".format(i)] = "balata shape circle"
		elif i == 8:
			d["0, {}".format(i)] = "balata color blue"
		else:
			d["0, {}".format(i)] = "balata"

	for i in range(9):
		if i == 5 or i == 7:
			d["1, {}".format(i)] = "wall"
		elif i in [2, 6]:
			pass
		else:
			d["1, {}".format(i)] = "balata"

	for i in range(9):
		if i == 2 or i == 1:
			d["2, {}".format(i)] = "wall"
		else:
			d["2, {}".format(i)] = "balata"

	for i in range(9):
		if i == 5 or i == 7 or i == 8:
			d["3, {}".format(i)] = "wall"
		else:
			d["3, {}".format(i)] = "balata"

	for i in range(9):
		if i == 0:
			d["4, {}".format(i)] = "balata color green"
		elif i == 8:
			d["4, {}".format(i)] = "balata color red"
		elif i in [2, 5]:
			d["4, {}".format(i)] = "wall"
		else:
			d["4, {}".format(i)] = "balata"

	for i in range(9):
		if i == 4:
			pass
		else:
			d["5, {}".format(i)] = "wall"

	for i in range(9):
		d["6, {}".format(i)] = "balata"

	for i in range(9):
		if i in [2, 6, 8]:
			pass
		elif i in [0, 1, 3, 5, 7]:
			d["7, {}".format(i)] = "wall"
		else:
			d["7, {}".format(i)] = "balata"

	for i in range(9):
		if i == 0:
			d["8, {}".format(i)] = "balata shape rect"
		elif i == 2:
			d["8, {}".format(i)] = "balata shape star"
		elif i == 6:
			d["8, {}".format(i)] = "balata color blue"
		elif i == 8:
			d["8, {}".format(i)] = "balata shape circle"
		elif i in [1, 3, 5, 7]:
			d["8, {}".format(i)] = "wall"
		else:
			d["8, {}".format(i)] = "balata"

	for i in range(9):
		if i == 8 or i == 0:
			pass
		elif i == 4:
			d["9, {}".format(i)] = "balata"
		else:
			d["9, {}".format(i)] = "wall"

	for i in range(9):
		d["10, {}".format(i)] = "balata"		

b1 = BALATA()
g1 = GATE("1, 2", "circle", "blue", "h")
g2 = GATE("1, 6", None, "red", "v")
g3 = GATE("1, 8", "circle", None, "v")
g4 = GATE("2, 0", "tri", None, "v")
g5 = GATE("3, 2", None, "green", "h")
g6 = GATE("3, 6", "rect", None, "v")
g7 = GATE("5, 4", "tri", "green", "v")
g8 = GATE("7, 2", "circle", "blue", "v")
g9 = GATE("7, 6", "rect", None, "v")
g10 = GATE("7, 8", "circle", None, "v")
g11 = GATE("9, 0", None, "green", "v")
g12 = GATE("9, 8", "rect", "blue", "v")
gateList = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12]

s = ZALATA("2, 4", "rect" ,"blue")

setDict()

def init( ):
	glClearColor (0.8, 0.8, 0.8, 0.0)
	glEnable(GL_DEPTH_TEST)
	glMatrixMode (GL_PROJECTION)
	glLoadIdentity ()
	glOrtho(0, 11, 0 , 12 , -1 , 1) # l,r,b,t,n,far

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

	elif setGate(g10):
		g10.open()
		s.setPassGate(True)

	elif setGate(g11):
		g11.open()
		s.setPassGate(True)

	elif setGate(g12):
		g12.open()
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
		g10.close()
		g11.close()
		g12.close()
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

def writeTextandtimer():
    shape = "SHAPE"
    writeStrokeText(4, 0.0055, shape, 2.5, 11, 1, 1, .1)
    switcher = "SWITCHER"
    writeStrokeText(4, 0.0055, switcher, 5, 11, 1, 0, 0)

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
	
	writeStrokeText(1.4, 0.003, t2string, 0.8, 10.3, 0.4, .2, 0.6)

	writeTextandtimer()

	openGates()

	glutSwapBuffers()

def keyboard(key, x, y):
	if key == b' ':
		import Level_4

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH )
init()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(s.move)
glutMainLoop()
