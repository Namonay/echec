import pygame as pg
import pygame.locals
import os
import sys
import time

file_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(file_dir, "ressources")

pg.init()
screen = pg.display.set_mode((500, 500))
pg.display.set_caption("Ehec")


# test
echiquier = pg.image.load(os.path.join(data_dir, 'echiquier.jpg'))
roib      = pg.image.load(os.path.join(data_dir, 'roi_blanc.png')) #6
roin      = pg.image.load(os.path.join(data_dir, 'roi_noir.png')) #12
pionb     = pg.image.load(os.path.join(data_dir, 'pion_blanc.png')) #1
pionn     = pg.image.load(os.path.join(data_dir, 'pion_noir.png')) #7
tourn     = pg.image.load(os.path.join(data_dir, 'tour_noir.png')) #8
tourb     = pg.image.load(os.path.join(data_dir, 'tour_blanc.png')) #2
foub      = pg.image.load(os.path.join(data_dir, 'fou_blanc.png')) #3
foun      = pg.image.load(os.path.join(data_dir, 'fou_noir.png')) #9
chevalb   = pg.image.load(os.path.join(data_dir, 'cheval_blanc.png')) #4
chevaln   = pg.image.load(os.path.join(data_dir, 'cheval_noir.png')) #10
reineb    = pg.image.load(os.path.join(data_dir, 'reine_blanc.png') )#5
reinen    = pg.image.load(os.path.join(data_dir, 'reine_noir.png')) #11


continuer = True
class Terrain:
    def __init__(self):
        self.terrain = [[0 for i in range(8)] for j in range(8)]
        self.terrain[1]=[7 for i in range(8)]
        self.terrain[6]=[1 for i in range(8)]
        self.terrain[0]=[8,10,9,12,11,9,10,8]
        self.terrain[7]=[2,4,3,5,6,3,4,2]
        
        
    def move(self,x,y,x2,y2):
        if x!=x2 or y!=y2:
            self.terrain[x2][y2]=self.terrain[x][y]
            self.terrain[x][y]=0
    
    def which_pressed(self):
        if pygame.mouse.get_pressed()[0]:
            x,y = pg.mouse.get_pos()
            x=int(x/62.5)
            y=int(y/62.5)
            return (y,x)
    def which_piece(self,x,i,j):
        if x==1 : screen.blit(pionb,(5+62.5*j,2+62.5*i))
        if x==2 : screen.blit(tourb,(5+62.5*j,2+62.5*i))
        if x==3 : screen.blit(foub,(5+62.5*j,2+62.5*i))
        if x==4 : screen.blit(chevalb,(5+62.5*j,2+62.5*i))
        if x==5 : screen.blit(reineb,(5+62.5*j,2+62.5*i))
        if x==6 : screen.blit(roib,(5+62.5*j,2+62.5*i))
        if x==7 : screen.blit(pionn,(5+62.5*j,2+62.5*i))
        if x==8 : screen.blit(tourn,(5+62.5*j,2+62.5*i))
        if x==9 : screen.blit(foun,(5+62.5*j,2+62.5*i))
        if x==10 : screen.blit(chevaln,(5+62.5*j,2+62.5*i))
        if x==11 : screen.blit(reinen,(5+62.5*j,2+62.5*i))
        if x==12 : screen.blit(roin,(5+62.5*j,2+62.5*i))
        
        
tristan=Terrain()
FPS_CLOCK = pygame.time.Clock()
px,py,npx,npy=None,None,None,None
while continuer:
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT or event.type== pg.KEYDOWN and event.key == pg.K_BACKSPACE:
            continuer = False
           
    screen.fill((0,0,0))
    screen.blit(echiquier,(0,0))
    for i in range(len(tristan.terrain)):
        
        for j in range(len(tristan.terrain[i])):
            
            x = tristan.terrain[i][j]
            tristan.which_piece(x, i, j)
    pygame.display.flip()
    print('PX :',px,'PY :',py,'NPX :',npx,'NPY :',npy)
    
    if pygame.mouse.get_pressed()[0] and px!=None and py!=None:
        
        npx,npy = tristan.which_pressed()
        print('PX :',px,'PY :',py,'NPX :',npx,'NPY :',npy)
        if px==npx and py==npy:
            npx,npy=None,None
            continue
        tristan.move(px,py,npx,npy)
        px,py,npx,npy = None,None,None,None
            
        pygame.time.wait(100)
        continue
        
    if pygame.mouse.get_pressed()[0] and px == None and py == None:
        px,py = tristan.which_pressed()
        if tristan.terrain[px][py]==0:
            px,py=None,None

    FPS_CLOCK.tick(30)
pg.quit()
