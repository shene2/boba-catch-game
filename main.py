import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boba Catch 🧋")

clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("arial", 26)
big_font = pygame.font.SysFont("arial", 48)

# Game states
MENU = "menu"
PLAYING = "playing"
GAME_OVER = "game_over"

state = MENU
difficulty = None

# Player
player_width = 60
player_height = 40
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 80
player_speed = 6

# Score & warnings
score = 0
warnings = 0

# Objects (initialized later)
boba_radius = 15
bad_radius = 15

def reset_objects(boba_speed, bad_speed):
    global boba_x, boba_y, bad_x, bad_y, boba_vel, bad_vel
    boba_x = random.randint(boba_radius, WIDTH - boba_radius)
    boba_y = -boba_radius
    bad_x = random.randint(bad_radius, WIDTH - bad_radius)
    bad_y = -bad_radius
    boba_vel = boba_speed
    bad_vel = bad_speed


running = True
while running:
    clock.tick(60)
    screen.fill((255, 230, 240))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # MENU INPUT
        if state == MENU and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                difficulty = "Easy"
                reset_objects(4, 5)
                state = PLAYING
            elif event.key == pygame.K_m:
                difficulty = "Medium"
                reset_objects(6, 7)
                state = PLAYING

        # RESTART
        if state == GAME_OVER and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                score = 0
                warnings = 0
                state = MENU

    # -------- MENU SCREEN --------
    if state == MENU:
        title = big_font.render("Boba Catch 🧋", True, (120, 60, 160))
        easy = font.render("Press E - Easy", True, (80, 80, 80))
        medium = font.render("Press M - Medium", True, (80, 80, 80))

        screen.blit(title, (WIDTH//2 - title.get_width()//2, 180))
        screen.blit(easy, (WIDTH//2 - easy.get_width()//2, 260))
        screen.blit(medium, (WIDTH//2 - medium.get_width()//2, 300))

    # -------- GAME PLAY --------
    if state == PLAYING:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        player_x = max(0, min(WIDTH - player_width, player_x))

        # Move objects
        boba_y += boba_vel
        bad_y += bad_vel

        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        boba_rect = pygame.Rect(boba_x - boba_radius, boba_y - boba_radius, boba_radius*2, boba_radius*2)
        bad_rect = pygame.Rect(bad_x - bad_radius, bad_y - bad_radius, bad_radius*2, bad_radius*2)

        # Catch boba
        if player_rect.colliderect(boba_rect):
            score += 1
            boba_y = -boba_radius
            boba_x = random.randint(boba_radius, WIDTH - boba_radius)

        # Catch wrong item
        if player_rect.colliderect(bad_rect):
            warnings += 1
            bad_y = -bad_radius
            bad_x = random.randint(bad_radius, WIDTH - bad_radius)
            if warnings >= 2:
                state = GAME_OVER

        # Reset if missed
        if boba_y > HEIGHT:
            boba_y = -boba_radius
            boba_x = random.randint(boba_radius, WIDTH - boba_radius)

        if bad_y > HEIGHT:
            bad_y = -bad_radius
            bad_x = random.randint(bad_radius, WIDTH - bad_radius)

        # UI
        screen.blit(font.render(f"Score: {score}", True, (80, 50, 120)), (20, 20))
        screen.blit(font.render(f"Warnings: {warnings}/1", True, (180, 60, 60)), (20, 50))
        screen.blit(font.render(f"Mode: {difficulty}", True, (80, 80, 80)), (20, 80))

        pygame.draw.rect(screen, (180, 120, 255), player_rect, border_radius=12)
        pygame.draw.circle(screen, (120, 80, 40), (boba_x, boba_y), boba_radius)
        pygame.draw.circle(screen, (200, 70, 70), (bad_x, bad_y), bad_radius)

    # -------- GAME OVER --------
    if state == GAME_OVER:
        over = big_font.render("GAME OVER", True, (150, 50, 50))
        restart = font.render("Press R to Restart", True, (80, 80, 80))

        screen.blit(over, (WIDTH//2 - over.get_width()//2, 240))
        screen.blit(restart, (WIDTH//2 - restart.get_width()//2, 290))

    pygame.display.update()

pygame.quit()
