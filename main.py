
import pygame
import os
import sys


from pygame.examples.moveit import HEIGHT

from stupid_image import bush_image, grass_image, grassleft_image

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1280
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
lvl = 'menu'
font = pygame.font.SysFont('aria', 40)



'def game_lvl():'





def restart():
    global bush_group, grassmens_group,mobs_groups,grass_group
    bush_group = pygame.sprite.Group()
    grassmens_group = pygame.sprite.Group()
    mobs_group = pygame.sprite.Group()
    grass_group = pygame.sprite.Group()

class Bush(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]



class Grass(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Enemy(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Tower(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Edit_dir_tile(pygame.sprite.Sprite):
    def __init__(self,image,pos,dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]







def drawmaps(nameFile):
    maps = []
    source = "game lvl/" + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 10):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])

    pos = [0,0]
    for i in range(0,len(maps)):
        pos[1] = i * 80
        for j in range(0,len(maps)):
            pos[0] = j * 80
            if maps[i][j] == '1':
                bush = Bush(bush_image,pos)
                bush_group.add(bush)
            elif maps[i][j] == '4':
                grass = Grass(grass_image,pos)
                grass_group.add(grass)
            elif maps[i][j] == '5':
                grassleft = Edit_dir_tile(grassleft_image,pos)
                Edit_dir_tile.add(grassleft)

















































































while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)








































