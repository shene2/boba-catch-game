import pygame

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

    # Drawing
    screen.fill((255, 230, 240))  # pastel pink background
    pygame.draw.rect(
        screen,
        (180, 120, 255),  # pastel purple
        (player_x, player_y, player_width, player_height),
        border_radius=12
    )

    pygame.display.update()

pygame.quit()
