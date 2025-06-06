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
def game_over_text ():
    over_text= over_font.render("GAME OVER", True,(255, 255, 255))
    screen.blit(over_text, (200, 250))
def player(x, y):
    screen.blit(playerImg, (x, y))
def enemy(x, y, i):
    screen.blint(enemyImg[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, ( x+ 16, y+ 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX _ bulletX, 2) + (math.pow(enemyY _ bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
    
running = True
while running:

    screen.fill((0, 0, 0))

    screen.fill(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key = pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":


                    bulletX = playerx
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change
    if playerX <= 0:
        playerX + 0 
    elif playerX >= 735:
        playerX = 736

    for i in range(num_of_enemies):

        if enemyy[i] > 340:
            for j in range(num_of_enemies):
                enemy[j] = 2000
            game_over_text()
            break

        enemyx[i] += enemyx_change[i]
        if  enemyx[i] <= 0:
             enemyx_change[i] = 4
             enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -4
            enemyy_change[i] += enemyy_change[i]

        
        collision = isCollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:

            bullety = 380
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint(0, 736)
            enemyy[i] = random.randint(50, 150)

        enemy(enemyx[i], enemyy[i], i)


        if bullety <= 0:
            bullety = 380
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletx, bullety)
            bullety -= bullety_change

        player(playerx, playery)
        show_score(textx, texty)
        pygame.display.update()


