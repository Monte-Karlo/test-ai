import pygame
import random
from datetime import datetime
from clGrass import *

zone_h = 5
zone_w = 15
zone_x0 = 5
zone_y0 = 5
plate_s = 50

pop_g = 15
pop_c = 5
pop_w = 3
gr = []
cw = []
wf = []
map = []

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

def mapr(x,y):
    z = int(map[y-1][x-1])
    return z
def mapw(x,y,z):
    map[y-1] = map[y-1][:(x-1)] + str(z) + map[y-1][x:]

def draw_plate():
    global sc
    pygame.draw.rect(sc, WHITE, (zone_x0+1, zone_y0+1, zone_w*plate_s-1, zone_h*plate_s-1))
    for i in range(zone_w-1):
        pygame.draw.line(sc,BLACK,[zone_x0+(i+1)*plate_s,zone_y0],[zone_x0+(i+1)*plate_s,zone_y0+zone_h*plate_s])
    for i in range(zone_h-1):
        pygame.draw.line(sc,BLACK,[zone_x0,zone_y0+(i+1)*plate_s],[zone_x0+zone_w*plate_s,zone_y0+(i+1)*plate_s])

def gen(k): #1-grass,2-cow,3-wolf
    global sc
    if k==1:
        gr=[]
        for i in range(pop_g):
            while 1:
                tx = random.randint(1,zone_w)
                ty = random.randint(1,zone_h)
                if mapr(tx,ty) == 0:
                    break
            mapw(tx,ty,1)
            print(map)
            gr.append(Grass(tx,ty))
            pygame.draw.rect(sc, GREEN, (zone_x0+1+(gr[i].x-1)*plate_s, zone_y0+1+(gr[i].y-1)*plate_s,plate_s-1, plate_s-1))

random.seed(datetime.now())
pygame.init()
txt=''
for i in range(zone_w):
    txt+='0'    
for i in range(5):
    map.append(txt)

sc = pygame.display.set_mode((zone_w*plate_s + 2*zone_x0, zone_h*plate_s + 2*zone_y0))
 
# здесь будут рисоваться фигуры
draw_plate()
gen(1)

print(map)

pygame.display.update()
 
while 1:
    pygame.time.delay(1000)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
