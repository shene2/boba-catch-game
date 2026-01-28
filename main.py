import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boba Catch 🧋")

# Clock
clock = pygame.time.Clock()

# Player settings
player_width = 60
player_height = 40
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 80
player_speed = 6

# Boba settings
boba_radius = 15
boba_x = random.randint(boba_radius, WIDTH - boba_radius)
boba_y = -boba_radius
boba_speed = 4

# Game loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player inside screen
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_width:
        player_x = WIDTH - player_width

    # Move boba
    boba_y += boba_speed

    # Reset boba if it goes off screen
    if boba_y > HEIGHT:
        boba_y = -boba_radius
        boba_x = random.randint(boba_radius, WIDTH - boba_radius)

    # Drawing
    screen.fill((255, 230, 240))  # pastel pink background

    # Draw player
    pygame.draw.rect(
        screen,
        (180, 120, 255),
        (player_x, player_y, player_width, player_height),
        border_radius=12
    )

    # Draw boba
    pygame.draw.circle(
        screen,
        (120, 80, 40),  # boba brown
        (boba_x, boba_y),
        boba_radius
    )

    pygame.display.update()

pygame.quit()
