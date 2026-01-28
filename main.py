import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boba Catch 🧋")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 26)
big_font = pygame.font.SysFont("arial", 48)

# Player
player_width = 60
player_height = 40
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 80
player_speed = 6

# Boba (GOOD object)
boba_radius = 15
boba_x = random.randint(boba_radius, WIDTH - boba_radius)
boba_y = -boba_radius
boba_speed = 4

# Distraction (BAD object)
bad_radius = 15
bad_x = random.randint(bad_radius, WIDTH - bad_radius)
bad_y = -bad_radius
bad_speed = 5

# Game state
score = 0
warnings = 0
game_over = False

# Game loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        player_x = max(0, min(WIDTH - player_width, player_x))

        # Move objects
        boba_y += boba_speed
        bad_y += bad_speed

        # Rectangles for collision
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        boba_rect = pygame.Rect(boba_x - boba_radius, boba_y - boba_radius, boba_radius*2, boba_radius*2)
        bad_rect = pygame.Rect(bad_x - bad_radius, bad_y - bad_radius, bad_radius*2, bad_radius*2)

        # Catch boba (GOOD)
        if player_rect.colliderect(boba_rect):
            score += 1
            boba_y = -boba_radius
            boba_x = random.randint(boba_radius, WIDTH - boba_radius)

        # Catch distraction (BAD)
        if player_rect.colliderect(bad_rect):
            warnings += 1
            bad_y = -bad_radius
            bad_x = random.randint(bad_radius, WIDTH - bad_radius)

            if warnings >= 2:
                game_over = True

        # Reset if missed
        if boba_y > HEIGHT:
            boba_y = -boba_radius
            boba_x = random.randint(boba_radius, WIDTH - boba_radius)

        if bad_y > HEIGHT:
            bad_y = -bad_radius
            bad_x = random.randint(bad_radius, WIDTH - bad_radius)

    # Drawing
    screen.fill((255, 230, 240))

    # UI text
    score_text = font.render(f"Score: {score}", True, (80, 50, 120))
    warn_text = font.render(f"Warnings: {warnings}/1", True, (180, 60, 60))
    screen.blit(score_text, (20, 20))
    screen.blit(warn_text, (20, 50))

    # Player
    pygame.draw.rect(screen, (180, 120, 255), player_rect, border_radius=12)

    # Boba (GOOD)
    pygame.draw.circle(screen, (120, 80, 40), (boba_x, boba_y), boba_radius)

    # Distraction (BAD)
    pygame.draw.circle(screen, (200, 70, 70), (bad_x, bad_y), bad_radius)

    # Game Over screen
    if game_over:
        over_text = big_font.render("GAME OVER", True, (150, 50, 50))
        info_text = font.render("You caught the wrong item twice!", True, (100, 0, 0))
        screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 40))
        screen.blit(info_text, (WIDTH//2 - info_text.get_width()//2, HEIGHT//2 + 10))

    pygame.display.update()

pygame.quit()
