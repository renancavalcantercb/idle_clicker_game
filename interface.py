import pygame
import config
from autoclickers import autoclickers


def draw_money():
    money_text = config.font.render(f"Money: ${config.game_money}", True, config.WHITE)
    config.screen.blit(money_text, (10, config.game_screen_height - 50))


def draw_save():
    save_text = config.font.render(f"Save", True, config.WHITE)
    config.screen.blit(
        save_text,
        (config.game_screen_width - 65, config.game_screen_height - 50),
    )


def draw_shop():
    x = 10
    y = config.game_screen_height - 300
    button_height = 30
    button_width = 200

    for color, autoclicker in autoclickers.items():
        if config.game_money >= autoclicker.cost:
            button_color = config.GREEN
        else:
            button_color = config.RED

        button_rect = pygame.Rect(x, y, button_width, button_height)
        pygame.draw.rect(config.screen, button_color, button_rect, 2)

        shop_text = config.font.render(
            f"{color.capitalize()} Autoclick: ${autoclicker.cost}",
            True,
            config.WHITE,
        )
        text_rect = shop_text.get_rect(center=button_rect.center)
        config.screen.blit(shop_text, text_rect)

        y += 40
