import pygame
import random
import math

# the directory to to my assets folder
dir = "GameDevelopment/game1 - pygame/assets/"

# Initialize a pygame
pygame.init()

# Creating the screen
gameWindowWidth = 800
gameWindowHeight = 600
screen = pygame.display.set_mode((gameWindowWidth,gameWindowHeight))

# Title and Icon
pygame.display.set_caption("Space Invaders Game1")
gameIcon = pygame.image.load(dir + "gamepad.png")
pygame.display.set_icon(gameIcon)

# Game Background
gameBackground = pygame.image.load(dir + "background.png")

# Player
playerImg = pygame.image.load(dir + "jet.png")
playerWidth = 64
playerX = 368
playerY = 510
playerSpeedX = 5
playerMovingLeft = False
playerMovingRight = False

# Enemy
enemyCount = 1
enemyImg = pygame.image.load(dir + "ghost.png")
enemyWidth = 64
enemyX = random.randint(0, gameWindowWidth-enemyWidth)
enemyY = random.randint(20, 50)
enemySpeedX = 3
enemyHit = False

# Bullet for shooting
bulletImg = pygame.image.load(dir + "bullet.png")
bulletX = playerX
bulletY = playerY
bulletIsFired = False
bulletSpeedX = 0 # unnecessary
bulletSpeedY = 10

# Defining functions -  blit is used for drawing on the screen
def DrawPlayer(x, y):
    screen.blit(playerImg, (x, y))

def DrawEnemy(x, y):
    global enemyHit

    if enemyHit == False:
        screen.blit(enemyImg, (x, y))
    else:
        RespawnEnemy()

def RespawnEnemy():
    global enemyX
    global enemyY

    enemyX = random.randint(0, gameWindowWidth-enemyWidth)
    enemyY = random.randint(20, 50)
    screen.blit(enemyImg, (enemyX, enemyY))

def FireTheBullet(x, y):
    screen.blit(bulletImg, (x+16, y+10))

def Player_Movement():
    global playerX

    if playerMovingRight and playerMovingLeft:
        playerX += 0
    elif playerMovingRight:
        playerX += playerSpeedX
    elif playerMovingLeft:
        playerX -= playerSpeedX

def Player_CheckBoundary():
    global playerX

    if playerX <= 0:
        playerX = 0
    elif playerX >= (gameWindowWidth - playerWidth):
        playerX = (gameWindowWidth - playerWidth)

def Enemy_Movement_CheckingBoundary():
    global enemyX
    global enemyY
    global enemySpeedX

    if enemyX <= 0 or enemyX >= (gameWindowWidth - enemyWidth):
        enemySpeedX *= -1
        enemyY += 64
    enemyX += enemySpeedX

def Bullet_Movement():
    global bulletIsFired
    global bulletX
    global bulletY

    if bulletIsFired:
        FireTheBullet(bulletX, bulletY)
        bulletY -= bulletSpeedY # for going up it is negative
        if bulletY <= 0:
            bulletIsFired = False
    elif bulletIsFired == False:
        bulletX = playerX
        bulletY = playerY

def CheckCollision_BulletToEnemy(enemyX, enemyY, bulletX, bulletY):
    dist = math.sqrt( (math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY-bulletY, 2)) )
    if dist <= enemyWidth/2:
        return True
    else:
        return False

# Game Loop
i_dont_want_to_quit_the_game = True
while i_dont_want_to_quit_the_game:
    # the screen's colour will be changed - layer1
    screen.fill((0,110,240)) # colours in RGB
    screen.blit(gameBackground, (0,0))

    # Checking for events 
    for event in pygame.event.get():
        # Checking if we are quitting the Game
        if event.type == pygame.QUIT:
            i_dont_want_to_quit_the_game = False

        # Player Movement - Checking if key is pressed'
        elif event.type == pygame.KEYDOWN:
            # Moving the player Left
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                playerMovingLeft = True
            # Moving the player Right
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                playerMovingRight = True
            # Firing the bullet
            if ((event.key == pygame.K_UP) or (event.key == pygame.K_w) or
            (event.key == pygame.K_SPACE)) and bulletIsFired == False:
                # print("The bullet is fired")
                # FireTheBullet(bulletX, bulletY)
                bulletIsFired = True
                FireTheBullet(bulletX, bulletY)
        # Player Movement - Checking if key is released
        elif event.type == pygame.KEYUP:
            # Player stops moving Left
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                playerMovingLeft = False
            # Player stops moving Right
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                playerMovingRight = False

    # Necessary function calls
    # Player - Movement        
    Player_Movement()
    # Player - Checking the boundary
    Player_CheckBoundary()
    # Checking the boundary - Enemy Movement
    Enemy_Movement_CheckingBoundary()
    # Bullet Movement
    Bullet_Movement()

    # Collision
    # Is the bullet hitting the Enemy
    enemyHit = (CheckCollision_BulletToEnemy(enemyX, enemyY, bulletX, bulletY))

    # Drawing the player to the screen - layer2
    DrawPlayer (playerX, playerY)
    # Drawing the enemy to the screen - layer3
    DrawEnemy (enemyX, enemyY)

    # Updates each frame of the Pygame
    pygame.display.update() # this must be the last line