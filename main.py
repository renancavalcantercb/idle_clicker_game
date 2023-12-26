import pygame

pygame.init()

# Color Library
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)


screen = pygame.display.set_mode((300, 450))
pygame.display.set_caption("Money Clicker")
BACKGROUND = BLACK
frame_rate = 60
font = pygame.font.SysFont("freesansbold.ttf", 16)
timer = pygame.time.Clock()


running = True


def draw_task(color, y_coord):
    pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, BLACK, [75, y_coord - 10, 190, 20])


while running:
    timer.tick(frame_rate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)
    draw_task(GREEN, 50)
    pygame.display.flip()


pygame.quit()
