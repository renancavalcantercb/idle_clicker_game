import pygame
from menu import draw_menu
from utils import save_game, load_game
from config import (
    BLACK,
    game_screen_width,
    game_screen_height,
    screen,
)
import config
from buttons import buttons
from autoclickers import autoclickers
from interface import draw_money, draw_shop, draw_save


running = True
menu_active = True
start_button, load_button = None, None

while running:
    if menu_active:
        menu_buttons = draw_menu()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, menu_button in enumerate(menu_buttons):
                    if menu_button.collidepoint(mouse_pos):
                        if i == 0:
                            menu_active = False
                        if i == 1:
                            load_game()
                            menu_active = False
                        if i == 2:
                            running = False

    else:
        config.timer.tick(config.frame_rate)
        screen.fill(BLACK)

        for button in buttons:
            button.draw(screen)
            button.draw_level(screen, config.font)
            button.update()

        for button_color, autoclicker in autoclickers.items():
            autoclicker.update(
                buttons[
                    buttons.index(
                        next(
                            filter(lambda b: b.button_color == button_color, buttons),
                            None,
                        )
                    )
                ]
            )

        draw_money()
        draw_shop()
        draw_save()
        save_button_rect = pygame.Rect(
            game_screen_width - 65, game_screen_height - 50, 60, 30
        )
        if save_button_rect.collidepoint(mouse_pos):
            save_game(config.game_money, autoclickers)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                for button in buttons:
                    if button.clicked(mouse_pos):
                        button.start_loading()

                y = game_screen_height - 300
                for color, autoclicker in autoclickers.items():
                    shop_item_rect = pygame.Rect(10, y, 200, 30)
                    if shop_item_rect.collidepoint(mouse_pos):
                        autoclicker.buy()
                    y += 40

        pygame.display.flip()

pygame.quit()
