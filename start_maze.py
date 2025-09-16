import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Maze Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Player
player_size = 20
player_x, player_y = 50, 50
player_speed = 5

# Maze walls (x, y, width, height)
walls = [
    pygame.Rect(100, 0, 20, 300),
    pygame.Rect(200, 100, 20, 300),
    pygame.Rect(300, 0, 20, 300)
]

# Goal
goal = pygame.Rect(350, 350, 30, 30)

# Game loop
running = True
while running:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Keypresses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
    # Player rectangle
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    
    # Collision with walls
    for wall in walls:
        if player_rect.colliderect(wall):
            if keys[pygame.K_LEFT]:
                player_x += player_speed
            if keys[pygame.K_RIGHT]:
                player_x -= player_speed
            if keys[pygame.K_UP]:
                player_y += player_speed
            if keys[pygame.K_DOWN]:
                player_y -= player_speed
    
    # Check goal
    if player_rect.colliderect(goal):
        print("You won!")
        running = False
    
    # Drawing
    win.fill(WHITE)
    for wall in walls:
        pygame.draw.rect(win, BLACK, wall)
    pygame.draw.rect(win, BLUE, player_rect)
    pygame.draw.rect(win, GREEN, goal)
    
    pygame.display.update()
