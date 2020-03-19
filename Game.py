import pygame
import random
import math

# initialising the game
pygame.init()
# creating the screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("C:/Users/benel_000/Desktop/Python/for finance/space.png")

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("C:/Users/benel_000/Desktop/Python/for finance/spaceship.png")
pygame.display.set_icon(icon)

# player start location
player_img = pygame.image.load("C:/Users/benel_000/Desktop/Python/for finance/spaceship.png")
player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0

# enemy start location


enemy_img = pygame.image.load("C:/Users/benel_000/Desktop/Python/for finance/asteroid.png")
enemy_x = random.randint(0, 800)
enemy_y = random.randint(50, 150)
enemy_x_change = 1
enemy_y_change = 1

# enemy2
enemy_img2 = pygame.image.load("C:/Users/benel_000/Desktop/Python/for finance/asteroid.png")
enemy_x2 = random.randint(0, 800)
enemy_y2 = random.randint(100, 200)
enemy_x_change2 = 1.5
enemy_y_change2 = 1.5

# enemy3
enemy_img3 = pygame.image.load("C:/Users/benel_000/Desktop/Python/for finance/asteroid.png")
enemy_x3 = random.randint(0, 800)
enemy_y3 = random.randint(50, 300)
enemy_x_change3 = 2
enemy_y_change3 = 2

# bullet start location
bullet_img = pygame.image.load("C:/Users/benel_000/Desktop/Python/for finance/bullet.png")
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 3.5
bullet_state = 'ready'

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


def enemy2(x, y):
    screen.blit(enemy_img2, (x, y))


def enemy3(x, y):
    screen.blit(enemy_img3, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_img, (x + 16, y + 10))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# player & enemy movement
running = True
while running:

    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # left and right movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -2
            if event.key == pygame.K_RIGHT:
                player_x_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         player_y_change = -0.1
        #     if event.key == pygame.K_DOWN:
        #         player_y_change = 0.1
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #         player_y_change = 0
        #         print('Keystroke was release')

    # player boundary
    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 768:
        player_x = 768

    player_y += player_y_change

    if player_y <= 0:
        player_y = 0
    elif player_y >= 568:
        player_y = 568

    # enemy boundary

    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 1
        enemy_x += enemy_x_change
    elif enemy_x >= 768:
        enemy_x_change = -1
        enemy_x += enemy_x_change

    if enemy_y <= 0:
        enemy_y_change = 1
        enemy_y += enemy_y_change
    elif enemy_y >= 568:
        enemy_y_change = -1
        enemy_y += enemy_y_change

    # enemy2
    enemy_x2 += enemy_x_change2
    if enemy_x2 <= 0:
        enemy_x_change2 = 1.5
        enemy_x2 += enemy_x_change2
    elif enemy_x2 >= 768:
        enemy_x_change2 = -1.5
        enemy_x2 += enemy_x_change2

    if enemy_y2 <= 0:
        enemy_y_change2 = 1.5
        enemy_y2 += enemy_y_change2
    elif enemy_y2 >= 568:
        enemy_y_change2 = -1.5
        enemy_y2 += enemy_y_change2

    # enemy3
    enemy_x3 += enemy_x_change3
    if enemy_x3 <= 0:
        enemy_x_change3 = 1
        enemy_x3 += enemy_x_change3
    elif enemy_x3 >= 768:
        enemy_x_change3 = -1
        enemy_x3 += enemy_x_change3

    if enemy_y3 <= 0:
        enemy_y_change3 = 1
        enemy_y3 += enemy_y_change3
    elif enemy_y3 >= 568:
        enemy_y_change3 = -1
        enemy_y3 += enemy_y_change3

    collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = 480
        bullet_state = 'ready'
        score_value += 1
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(50, 150)

        enemy(enemy_x, enemy_y)

    # enemy2
    collision = is_collision(enemy_x2, enemy_y2, bullet_x, bullet_y)
    if collision:
        bullet_y = 480
        bullet_state = 'ready'
        score_value += 1
        enemy_x2 = random.randint(0, 736)
        enemy_y2 = random.randint(50, 150)

        enemy(enemy_x2, enemy_y2)

    # enemy 3
    collision = is_collision(enemy_x3, enemy_y3, bullet_x, bullet_y)
    if collision:
        bullet_y = 480
        bullet_state = 'ready'
        score_value += 1
        enemy_x3 = random.randint(0, 736)
        enemy_y3 = random.randint(50, 150)

        enemy(enemy_x3, enemy_y3)

    # Bullet state
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # collision

    player(player_x, player_y)
    show_score(textX,textY)
    enemy(enemy_x, enemy_y)
    enemy2(enemy_x2, enemy_y2)
    enemy3(enemy_x3, enemy_y3)
    pygame.display.update()

