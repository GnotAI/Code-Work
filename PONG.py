import pygame, sys, random

def ball_anim():
    global bsx, bsy
    ball.x += bsx
    ball.y += bsy

    if ball.top <= 0 or ball.bottom >= screen_h:
        bsy *= -1
    if ball.left <= 0 or ball.right >= screen_w:
        bsx = bsy
        bsy = bsx
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        bsx *= -1.1
#border control
def player_anim():
    player.y += player_s
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_h:
        player.bottom = screen_h

def opponent_anim():
    opponent.y += opponent_s
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_h:
        opponent.bottom = screen_h

#restarting
def ball_restart():
    global bsx, bsy
    ball.center = (screen_w/2, screen_h/2)
    bsx *= random.choice((1, -1))
    bsy *= random.choice((1, -1))

#general setup
pygame.init()
clock = pygame.time. Clock()

#setting the main window
screen_w = 1400
screen_h = 800
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('PONG')

#game rects.
ball = pygame.Rect(screen_w/2 - 15, screen_h/2 - 15, 30, 30)
player = pygame.Rect(screen_w - 20, screen_h/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_h/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

bsx = 7 * random.choice((1, -1))
bsy = 7 * random.choice((1, -1))
player_s = 0
opponent_s = 0


while True:
    #handlilng input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                pygame.quit()
                sys.exit()

        #player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_s += 7
            if event.key == pygame.K_UP:
                  player_s -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_s -= 7
            if event.key == pygame.K_UP:
                  player_s += 7

        #opponent movemenet
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                opponent_s -= 7
            if event.key == pygame.K_s:
                opponent_s += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                opponent_s -= 7
            if event.key == pygame.K_w:
                opponent_s += 7


    ball_anim()
    player_anim()
    opponent_anim()

    #visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_w/2, 0), (screen_w/2, screen_h))


    #updating the window
    pygame.display.flip()
    clock.tick(60)
