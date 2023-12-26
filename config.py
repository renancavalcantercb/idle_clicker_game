import pygame

game_font = "freesansbold.ttf"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)


game_money = 0
game_screen_width = 360
game_screen_height = 640
screen = pygame.display.set_mode((game_screen_width, game_screen_height))

pygame.init()

pygame.display.set_caption("Money Clicker")
font = pygame.font.SysFont("freesansbold.ttf", 24)
timer = pygame.time.Clock()
frame_rate = 60
