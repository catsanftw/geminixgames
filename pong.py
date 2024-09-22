import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")

# Ball properties
ball_color = (255, 0, 0)  # Red
ball_radius = 15
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_x_speed = 5
ball_y_speed = 5

# Frame rate control
clock = pygame.time.Clock()
fps = 30  # Target frame rate (adjust as needed)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Bounce off the walls
    if ball_x + ball_radius > screen_width or ball_x - ball_radius < 0:
        ball_x_speed = -ball_x_speed
    if ball_y + ball_radius > screen_height or ball_y - ball_radius < 0:
        ball_y_speed = -ball_y_speed

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(fps)

# Quit Pygame
pygame.quit()
