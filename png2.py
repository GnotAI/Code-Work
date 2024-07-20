import pygame, sys, random

# Define score variable
score_player = 0
score_opponent = 0

# Define game constants
screen_width = 1400
screen_height = 800
ball_radius = 30
player_radius = 10
opponent_radius = 10
player_speed = 7
opponent_speed = 7

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Define fonts
font_large = pygame.font.Font("/usr/share/fonts/TTF/BAUHS93.TTF", 72)
font_medium = pygame.font.Font("/usr/share/fonts/TTF/BAUHS93.TTF", 48)
font_small = pygame.font.Font("/usr/share/fonts/TTF/BAUHS93.TTF", 36)

# Define game objects
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PONG")
ball = pygame.draw.circle(screen, white, (screen_width//2, screen_height//2), ball_radius)
player = pygame.draw.circle(screen, blue, (screen_width-player_radius, screen_height//2), player_radius)
opponent = pygame.draw.circle(screen, red, (player_radius, screen_height//2), opponent_radius)

# Define game logic
def ball_movement(ball, player, opponent, player_speed, opponent_speed):
    # Calculate ball movement
    ball.x += ball.x_speed
    ball.y += ball.y_speed

    # Check for ball collision with walls
    if ball.y <= ball_radius:
        ball.y = ball_radius
        ball.y_speed *= -1
    if ball.y >= screen_height-ball_radius:
        ball.y = screen_height-ball_radius-1
        ball.y_speed *= -1
    if ball.x <= ball_radius:
        ball.x = ball_radius
        ball.x_speed *= -1
    if ball.x >= screen_width-ball_radius:
        ball.x = screen_width-ball_radius-1
        ball.x_speed *= -1

    # Check for ball collision with player
    if pygame.Rect.colliderect(player, ball):
        ball.x_speed *= -1
        score_player += 1
        ball.y_speed = random.uniform(-5, 5)

    # Check for ball collision with opponent
    if pygame.Rect.colliderect(opponent, ball):
        ball.x_speed *= -1
        score_opponent += 1
        ball.y_speed = random.uniform(-5, 5)

def player_movement(player, screen_height, player_speed):
    # Check for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Check for player collision with walls
    if player.y <= 0:
        player.y = 0
    if player.y >= screen_height-player_radius:
        player.y = screen_height-player_radius

def game_over_screen(screen, font, text, color):
    # Display game over screen
    screen.fill(color)
    text = font.render(text, True, white)
    screen.blit(text, (screen_width//2-text.get_width()//2, screen_height//2-text.get_height()//2))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move game objects
    ball_movement(ball, player, opponent, player_speed, opponent_speed)
    player_movement(player, screen_height, player_speed)

    # Check for game over
    if score_player >= 11:
        game_over_screen(screen, font_large, "Player Wins!", red)
        running = False
    elif score_opponent >= 11:
        game_over_screen(screen, font_large, "Computer Wins!", blue)
        running = False

    # Draw game objects
    screen.fill(black)
    pygame.draw.circle(screen, white, (screen_width//2, screen_height//2), ball_radius)
    pygame.draw.circle(screen, blue, (screen_width-player_radius, screen_height//2), player_radius)
    pygame.draw.circle(screen, red, (player_radius, screen_height//2), opponent_radius)
    text_player = font_medium.render(str(score_player), True, white)
    text_opponent = font_medium.render(str(score_opponent), True, white)
    screen.blit(text_player, (screen_width-text_player.get_width(), screen_height-text_player.get_height()))
    screen.blit(text_opponent, (player_radius, screen_height-text_opponent.get_height()))

    # Update screen
    pygame.display.flip()

# Close game window
pygame.quit()
sys.exit()