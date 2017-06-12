from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from Global import *
from Balata import BALATA
from Gate import GATE
from Zalata import ZALATA
import pygame
from pygame import mixer 		# for sounds

# fill dictionary function
def setDict():
	for i in range(9):                      # "x, y" --> value
		d["0, {}".format(i)] = "wall"

	for i in range(9):
		if i == 4:
			d["10, {}".format(i)] = "balata shape star"
		else:
			d["10, {}".format(i)] = "wall"

	for i in range(1, 10):
		d["{}, 0".format(i)] = "wall"

	for i in range(1, 10):
		d["{}, 8".format(i)] = "wall"

	for i in range(1, 8):
		d["1, {}".format(i)] = "balata"

	for i in range(1, 8):
		if i == 3 or i == 4 or i == 5:
			d["2, {}".format(i)] = "balata"
		else:
			d["2, {}".format(i)] = "wall"

	for i in range(1, 8):
		if i == 1 or i == 7:
			d["3, {}".format(i)] = "balata"
		elif i == 4:
			pass
		else:
			d["3, {}".format(i)] = "wall"

	for i in range(1, 8):
		d["4, {}".format(i)] = "balata"

	for i in range(1, 8):
		if i in [1, 4, 7]:
			d["5, {}".format(i)] = "balata"
		else:
			d["5, {}".format(i)] = "wall"

	for i in range(1, 8):
		if i in [3, 5]:
			d["6, {}".format(i)] = "wall"
		elif i == 2:
			d["6, {}".format(i)] = "balata shape tri"
		elif i == 6:
			d["6, {}".format(i)] = "balata color red"
		else:
			d["6, {}".format(i)] = "balata"

	for i in range(1, 8):
		if i in [1, 4, 7]:
			d["7, {}".format(i)] = "balata"
		else:
			d["7, {}".format(i)] = "wall"

	for i in range(1, 8):
		d["8, {}".format(i)] = "balata"

	for i in range(1, 8):
		if i in [3, 5]:
			d["9, {}".format(i)] = "wall"
		elif i == 4:
			pass
		else:
			d["9, {}".format(i)] = "balata"

	d["11, 4"] = "wall"

# initiate an instance of BALATA
b1 = BALATA()

# gate instances
# position, shape drawn, color, direction
g1 = GATE("3, 4", "circle", "green", "v")       # "v" --> the gate is vertical
g2 = GATE("9, 4", "tri", "red", "v")

# position, shape, color
s = ZALATA("1, 4", "circle" ,None)

# call once
setDict()


def init( ):
	glClearColor (0.8, 0.8, 0.8, 0.0) # background color
	glEnable(GL_DEPTH_TEST)           # enable Z-BUFFER
	glMatrixMode (GL_PROJECTION)
	glLoadIdentity ()
	# seen coordinates
	glOrtho(0, 11, 0 , 11 , -1 , 1) # l,r,b,t,n,f

	# for textures
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

	mixer.init()
	mixer.music.load("Marimba Boy.wav")
	mixer.music.play(-1)


# text functions
def writeStrokeText(width, scale, string, x, y, r, g, b):
	glLineWidth(width)
	glColor(r, g, b)  # Yellow Color
	glLoadIdentity()
	glTranslate(x, y, 0)
	glScale(scale, scale, 1)
	string = string.encode()  # conversion from Unicode string to byte string
	for c in string:
		glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def gameName():
	shape = "SHAPE"
	writeStrokeText(4, 0.0055, shape, 2.5, 10, 1, 1, .1)
	switcher = "SWITCHER"
	writeStrokeText(4, 0.0055, switcher, 5, 10, 1, 0, 0)

	# eplaysound("bomb.mp3")
	# pygame.mixer.music.load("bomb.mp3")
	# pygame.mixer.music.play()

# draw what in dict
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

# defines when gates is opened/closed
def setGate(gate):
	x1 = indexDec(s.getIndex())     # Zalata position
	x2 = indexDec(gate.getIndex())  # Gate position
	if gate.getDirection() == "v":  # Gate is vertical
		if gate.getColor() == None:
			b = x1[0] in np.arange(x2[0] - 1, x2[0] + 1.25, 0.25) \
			and x1[1] in np.arange(x2[1], x2[1] + 1.25, 0.25) \
			and s.getShape() == gate.getShape()
			return b                # b is boolean
		else:
			if gate.getShape() == None:
				b = x1[0] in np.arange(x2[0] - 1, x2[0] + 1.25, 0.25) \
				and x1[1] in np.arange(x2[1], x2[1] + 1.25, 0.25) \
				and s.getColor() == gate.getColor()
				return b
			else:
				b = x1[0] in np.arange(x2[0] - 1, x2[0] + 1.25, 0.25) \
				and x1[1] in np.arange(x2[1], x2[1] + 1.25, 0.25) \
				and s.getColor() == gate.getColor() \
				and s.getShape() == gate.getShape()
				return b
	else:
		if gate.getColor() == None:
			b = x1[0] in np.arange(x2[0], x2[0] + 1.25, 0.25) \
			and x1[1] in np.arange(x2[1] - 1, x2[1] + 1.25, 0.25) \
			and s.getShape() == gate.getShape()
			return b
		else:
			if gate.getShape() == None:
				b = x1[0] in np.arange(x2[0], x2[0] + 1.25, 0.25) \
				and x1[1] in np.arange(x2[1] - 1, x2[1] + 1.25, 0.25) \
				and s.getColor() == gate.getColor()
				return b
			else:
				b = x1[0] in np.arange(x2[0], x2[0] + 1.25, 0.25) \
				and x1[1] in np.arange(x2[1] - 1, x2[1] + 1.25, 0.25) \
				and s.getColor() == gate.getColor() \
				and s.getShape() == gate.getShape()
				return b

# draw gates in their places
def drawGate(gate):
	b1.draw(gate.getIndex())        # draw Balata beneath the Gate
	gate.draw()                     # draw Gate
	gate.setShape()                 # set & draw shape of Gate

# open/close gates
def openGates():

	if setGate(g1):                 # check condtion for gate 1
		g1.open()                   # open if setGate() is True
		s.setPassGate(True)         # let Zalata pass gate

	elif setGate(g2):
		g2.open()
		s.setPassGate(True)

	else:
		g1.close()                  # close all gates if opened
		g2.close()
		s.setPassGate(True)        # Zalata cannot pass any gate


def draw():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

	# display scene
	drawDict()

	# draw gates
	drawGate(g1)
	drawGate(g2)

	# draw zalata
	s.draw()

	# open/close the gates
	openGates()

	# text on top   
	l = indexDec(s.getIndex())
	x = "{}, {}".format(round(l[0]), round(l[1]))
	if d[x] == "balata shape star":
		t2string =  "BRAVO!.. press space to continue"
		glutKeyboardFunc(keyboard)
	else:
		t2string = "Collect required shapes/colors to cross the gates"
	
	writeStrokeText(1.4, 0.003, t2string, 0.8, 9.3, 0.4, .2, 0.6)

	gameName()

	glutSwapBuffers()

def keyboard(key, x, y):
	if key == b' ': # SPACE key
		import Level_2              # move to the next level
		glDeleteTextures(texture)   # delete textures


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH )
glutInitWindowSize(700, 700)
glutInitWindowPosition(200, 45)
glutCreateWindow(b"Shpae Switcher - Level 1")
init()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(s.move) # zalata movement
glutMainLoop()
