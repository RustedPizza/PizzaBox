# RustedPizza 2021
# Use WASD to move left, right, up and down
# Press space to go up
# Press Left Shift to go down
# Math taken from here: https://en.wikipedia.org/wiki/3D_projection

from random import *
from math import sin,cos
import pygame as pg

pg.init(); pg.font.init()
gD = pg.display.set_mode((800,600))
pg.display.set_caption("3D Demo")

class Line3:
    def __init__(self,sx,sy,sz,ex,ey,ez):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.ex = ex
        self.ey = ey
        self.ez = ez

c = pg.math.Vector3(250,250,250)
t = pg.math.Vector3(250,250,250)
e = pg.math.Vector3(250,250,250)
sd = pg.math.Vector3(0,0,0)
ed = pg.math.Vector3(0,0,0)
sb = pg.math.Vector2(0,0)
eb = pg.math.Vector2(0,0)

lineArray = [0] * 9

lineArray[0] = Line3(300,300,300,300,400,300)
lineArray[1] = Line3(300,300,300,300,300,400)
lineArray[2] = Line3(300,300,300,350,350,350)
lineArray[3] = Line3(300,400,400,300,300,400)
lineArray[4] = Line3(300,400,400,300,400,300)
lineArray[5] = Line3(300,400,400,350,350,350)
lineArray[6] = Line3(300,300,400,350,350,350)
lineArray[7] = Line3(300,400,300,350,350,350)
lineArray[8] = Line3(300,400,400,350,350,350)

crashed = False
while not crashed:

    gD.fill((0,0,0))
    
    for event in pg.event.get():
        if event.type == pg.QUIT: crashed = True

    pressed = pg.key.get_pressed()
    if pressed[pg.K_SPACE]:  c.x -= 0.1
    if pressed[pg.K_LSHIFT]: c.x += 0.1
    if pressed[pg.K_s]:      c.y -= 0.1
    if pressed[pg.K_w]:      c.y += 0.1
    if pressed[pg.K_a]:      c.z -= 0.1
    if pressed[pg.K_d]:      c.z += 0.1

    myfont = pg.font.SysFont('Helvetica',10)
    textsurface = myfont.render('Pyramid',True,(0,255,0))
    gD.blit(textsurface,(5,5))

    for x in range(0,len(lineArray)-1):
        
        oSX = lineArray[x].sx - c.x
        oSY = lineArray[x].sy - c.y
        oSZ = lineArray[x].sz - c.z
        oEX = lineArray[x].ex - c.x
        oEY = lineArray[x].ey - c.y
        oEZ = lineArray[x].ez - c.z
        
        cosx = cos(t.x)
        cosy = cos(t.y)
        cosz = cos(t.z)
        sinx = sin(t.x)
        siny = sin(t.y)
        sinz = sin(t.z)

        sd.x = cosy*(sinz*oSY+cosz*oSX)-siny*oSZ
        sd.y = sinx*(cosy*oSZ+siny*(sinz*oSY+cosz*oSX))+cosx*(cosz*oSY-sinz*oSX)
        sd.z = cosx*(cosy*oSZ+siny*(sinz*oSY+cosz*oSX))-sinx*(cosz*oSY-sinz*oSX)
        ed.x = cosy*(sinz*oEY+cosz*oEX)-siny*oEZ
        ed.y = sinx*(cosy*oEZ+siny*(sinz*oEY+cosz*oEX))+cosx*(cosz*oEY-sinz*oEX)
        ed.z = cosx*(cosy*oEZ+siny*(sinz*oEY+cosz*oEX))-sinx*(cosz*oEY-sinz*oEX)

        sb.x = sd.x*(e.z/sd.z) + e.x
        sb.y = sd.y*(e.z/sd.z) + e.y
        eb.x = ed.x*(e.z/ed.z) + e.x
        eb.y = ed.y*(e.z/ed.z) + e.y

        pg.draw.line(gD,(0,255,0),sb,eb)

    pg.display.update()

pg.quit()
