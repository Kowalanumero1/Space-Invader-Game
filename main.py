import mmath
import random
import pygame


pygame.init()

screen = pygame.display.set_mode((800, 500))


pygame.display.set_caption("space invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

pygameImg = pygame.image.load('player.png')
playerx=370
playery=380
playerx_change = 0

enemyImg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randit(0, 736))
    enemyy.append(random.randit(50, 150))
    enemyx_change.append(4)
    enemyy_change.append(40)



bulletingImg=pygame.image.load('bullet.png')
bulletx = 0
bullety = 380
bulletx_change= 0
bullety_change= 10
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10

over_font =pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    score = font.render("scare : " + str    (score_value, True, (255, 255, 255)
                                                 screen.blit)(score,(x, y)))
