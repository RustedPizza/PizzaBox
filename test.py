# Use WASD and the arrow keys to move the 2 points
# It is possible for the points to have negative coordinates or leave the screen

import pygame as pg

pg.init(); pg.font.init()

sW = 600; sH = 600	# Screen Width and Height
CLR = (0,255,0)		# Pen Color
pW = 1				# Pen Width
gD = pg.display.set_mode((sW, sH))
pygame.display.set_caption("Demo")

def In(x, upper, lower):
	if x < upper and x > lower: return True
	else: return False

def Draw(a, b):
	pg.draw.line(gD, CLR, a, b, pW)
	pg.display.update()

p1 = pg.math.Vector2(300, 300)	# Input coordinates
p2 = pg.math.Vector2(300, 300)
r1 = pg.Vector2(0, 0)			# Resulting points for pygame
r2 = pg.Vector2(0, 0)

p1Out = True; p2Out = True

crashed = False
while not crashed:

	gD.fill((0,0,0))
	myfont = pg.font.SysFont('Helvetica',10)
	p1_font = myfont.render(str(round(p1.x)) + "," + str(round(p1.y)), True, CLR)
	p2_font = myfont.render(str(round(p2.x)) + "," + str(round(p2.y)), True, CLR)
	r1_font = myfont.render(str(round(r1.x)) + "," + str(round(r1.y)), True, CLR)
	r2_font = myfont.render(str(round(r2.x)) + "," + str(round(r2.y)), True, CLR)
	gD.blit(p1_font, (5, 5))
	gD.blit(p2_font, (5, 15))
	gD.blit(r1_font, (5, 25))
	gD.blit(r2_font, (5, 35))

	for event in pg.event.get():
		if event.type == pg.QUIT: crashed = True

	pressed = pg.key.get_pressed()
	if pressed[pg.K_w]:     p1.y -= 0.1
	if pressed[pg.K_s]:     p1.y += 0.1
	if pressed[pg.K_a]:     p1.x -= 0.1
	if pressed[pg.K_d]:     p1.x += 0.1
	if pressed[pg.K_UP]:    p2.y -= 0.1
	if pressed[pg.K_DOWN]:  p2.y += 0.1
	if pressed[pg.K_LEFT]:  p2.x -= 0.1
	if pressed[pg.K_RIGHT]: p2.x += 0.1

	LEFT  = False
	RIGHT = False
	UP    = False
	DOWN  = False

	m = (p2.y - p1.y) / (p2.x - p1.x + 0.0001)
	if In(p1.x, sW, 0) and In(p1.y, sH, 0): p1Out = False
	if In(p2.x, sW, 0) and In(p2.y, sH, 0): p2Out = False
	if not p1Out and not p2Out: r1 = p1; r2 = p2
	Lsecy = m * (0  - p2.x) + p2.y
	Rsecy = m * (sW - p2.x) + p2.y
	Usecx = ((0  - p2.y) / (m + 0.0001)) + p2.x
	Dsecx = ((sH - p2.y) / (m + 0.0001)) + p2.x
	max_x = max(p1.x, p2.x)
	max_y = max(p1.y, p2.y)
	min_x = min(p1.x, p2.x)
	min_y = min(p1.y, p2.y)
	if In(Lsecy, max_y, min_y): LEFT  = True
	if In(Rsecy, max_y, min_y): RIGHT = True
	if In(Usecx, max_x, min_x): UP    = True
	if In(Dsecx, max_x, min_x): DOWN  = True
	if LEFT and UP:
		r1.x = 0
		r1.y = Lsecy
		r2.x = Usecx
		r2.y = 0
	elif LEFT and DOWN:
		r1.x = 0
		r1.y = Lsecy
		r2.x = Dsecx
		r2.y = sH
	elif RIGHT and UP:
		r1.x = sW
		r1.y = Rsecy
		r2.x = Usecx
		r2.y = 0
	elif RIGHT and DOWN:
		r1.x = sW
		r1.y = Rsecy
		r2.x = Dsecx
		r2.y = sH
	elif LEFT:
		if p1Out:
			r1.x = 0
			r1.y = Lsecy
			r2 = p2
		elif p2Out:
			r2.x = 0
			r2.y = Lsecy
			r1 = p1
	elif RIGHT:
		if p1Out:
			r1.x = sW
			r1.y = Rsecy
			r2 = p2
		elif p2Out:
			r2.x = sW
			r2.y = Rsecy
			r1 = p1
	elif UP:
		if p1Out:
			r1.x = Usecx
			r1.y = 0
			r2 = p2
		elif p2Out:
			r2.x = Usecx
			r2.y = 0
			r1 = p1
	elif DOWN:
		if p1Out:
			r1.x = Dsecx
			r1.y = sH
			r2 = p2
		elif p2Out:
			r2.x = Dsecx
			r2.y = sH
			r1 = p1

	Draw(r1, r2)

pg.quit()
