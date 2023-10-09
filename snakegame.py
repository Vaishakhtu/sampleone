import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SNAKE_SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake variables
snake_x = GRID_WIDTH // 2
snake_y = GRID_HEIGHT // 2
snake_body = [(snake_x, snake_y)]
snake_direction = 'RIGHT'

# Food variables
food_x = random.randint(0, GRID_WIDTH - 1)
food_y = random.randint(0, GRID_HEIGHT - 1)

# Score
score = 0

# Game over flag
game_over = False

# Main game loop
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'

    # Move the snake
    if snake_direction == 'UP':
        snake_y -= 1
    elif snake_direction == 'DOWN':
        snake_y += 1
    elif snake_direction == 'LEFT':
        snake_x -= 1
    elif snake_direction == 'RIGHT':
        snake_x += 1

    # Check for collisions with food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = random.randint(0, GRID_WIDTH - 1)
        food_y = random.randint(0, GRID_HEIGHT - 1)
        snake_body.append((snake_x, snake_y))

    # Check for collisions with walls or itself
    if (
        snake_x < 0
        or snake_x >= GRID_WIDTH
        or snake_y < 0
        or snake_y >= GRID_HEIGHT
        or (snake_x, snake_y) in snake_body[:-1]
    ):
        game_over = True

    # Update the snake's body
    snake_body.append((snake_x, snake_y))
    if len(snake_body) > score + 1:
        del snake_body[0]

    # Clear the screen
    screen.fill(BLACK)

    # Draw the food
    pygame.draw.rect(
        screen, GREEN, pygame.Rect(food_x * GRID_SIZE, food_y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(
            screen, WHITE, pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()
