import pygame
from config import WHITE, game_screen_width, screen, game_font, BLUE


def draw_menu():
    options = ["Start", "Load Progress", "Quit"]
    screen_width = game_screen_width
    font = pygame.font.SysFont(game_font, 24)

    buttons = []
    y_position = 150
    button_width = 150
    button_height = 50

    header = font.render("Cookie Clicker", False, WHITE)
    header_rect = header.get_rect(center=(screen_width / 2, 50))
    screen.blit(header, header_rect)

    for option in options:
        x_position = screen_width / 2 - button_width / 2

        button_rect = pygame.Rect(x_position, y_position, button_width, button_height)
        pygame.draw.rect(screen, BLUE, button_rect)

        text = font.render(option, True, WHITE)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

        buttons.append(button_rect)

        y_position += 100

    footer = font.render("Made by: CuTGuArDiAn Studios", False, WHITE)
    footer_rect = footer.get_rect(center=(screen_width / 2, 500))
    screen.blit(footer, footer_rect)

    return buttons
