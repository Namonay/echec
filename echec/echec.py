import pygame as pg
import pygame.locals
import os


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
        self.terrain[0]=[8,9,10,12,11,10,9,8]
        self.terrain[7]=[2,3,4,5,6,4,3,2]
        
        
    def move(self,x,y,x2,y2):
        self.terrain[x2][y2]=self.terrain[x][y]
        self.terrain[x][y]=0
    
tristan=Terrain()
while continuer:
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            continuer = False
           
    screen.fill((0,0,0))
    screen.blit(echiquier,(0,0))
    
    for y in range(len(tristan.terrain)):
        for x in tristan.terrain[y]:
            if x==1 : screen.blit(pionb,(62*x,62*y))
            if x==2 : screen.blit(tourb,(62*x,62*y))
            if x==3 : screen.blit(foub,(62*x,62*y))
            if x==4 : screen.blit(chevalb,(62*x,62*y))
            if x==5 : screen.blit(reineb,(62*x,62*y))
            if x==6 : screen.blit(roib,(62*x,62*y))
            if x==7 : screen.blit(pionn,(62*x,62*y))
            if x==8 : screen.blit(tourn,(62*x,62*y))
            if x==9 : screen.blit(foun,(62*x,62*y))
            if x==10 : screen.blit(chevaln,(62*x,62*y))
            if x==11 : screen.blit(reinen,(62*x,62*y))
            if x==12 : screen.blit(roin,(62*x,62*y))
            
    
    pygame.display.flip()
    
pg.quit()
