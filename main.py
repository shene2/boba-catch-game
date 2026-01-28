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

# Font
font = pygame.font.SysFont("arial", 28)

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

# Score
score = 0

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

    # Player rectangle (for collision)
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    boba_rect = pygame.Rect(
        boba_x - boba_radius,
        boba_y - boba_radius,
        boba_radius * 2,
        boba_radius * 2
    )

    # Collision detection
    if player_rect.colliderect(boba_rect):
        score += 1
        boba_y = -boba_radius
        boba_x = random.randint(boba_radius, WIDTH - boba_radius)

    # Reset boba if missed
    if boba_y > HEIGHT:
        boba_y = -boba_radius
        boba_x = random.randint(boba_radius, WIDTH - boba_radius)

    # Drawing
    screen.fill((255, 230, 240))  # background

    # Draw score
    score_text = font.render(f"Score: {score}", True, (80, 50, 120))
    screen.blit(score_text, (20, 20))

    # Draw player
    pygame.draw.rect(
        screen,
        (180, 120, 255),
        player_rect,
        border_radius=12
    )

    # Draw boba
    pygame.draw.circle(
        screen,
        (120, 80, 40),
        (boba_x, boba_y),
        boba_radius
    )

    pygame.display.update()

pygame.quit()
