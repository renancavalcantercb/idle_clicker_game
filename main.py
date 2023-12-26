import pygame
from menu import draw_menu
from utils import save_game, load_game

pygame.init()

# Color Library
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# Game Variables
money = 0
screen_width = 360
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Money Clicker")
font = pygame.font.SysFont("freesansbold.ttf", 24)
timer = pygame.time.Clock()
frame_rate = 60


class Button:
    def __init__(self, color, pos, value, button_color):
        self.color = color
        self.pos = pos
        self.radius = 20
        self.value = value
        self.progress = 0
        self.max_progress = 100 * self.value
        self.is_loading = False
        self.button_color = button_color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        if self.is_loading:
            prog_rect = pygame.Rect(
                self.pos[0] + 35,
                self.pos[1] - 10,
                (200 * self.progress) // self.max_progress,
                20,
            )
            pygame.draw.rect(screen, self.color, prog_rect)

    def draw_level(self, screen, font):
        if self.button_color in autoclickers:
            level = autoclickers[self.button_color].level
            level_text = font.render(f"{level}", True, WHITE)

            text_rect = level_text.get_rect(center=(self.pos[0], self.pos[1]))

            screen.blit(level_text, text_rect)

    def update(self):
        if self.is_loading and self.progress < self.max_progress:
            self.progress += 1
        elif self.progress >= self.max_progress:
            global money
            money += self.get_value()
            self.progress = 0
            self.is_loading = False

    def clicked(self, mouse_pos):
        distance = (
            (mouse_pos[0] - self.pos[0]) ** 2 + (mouse_pos[1] - self.pos[1]) ** 2
        ) ** 0.5
        return distance <= self.radius

    def start_loading(self):
        if not self.is_loading:
            self.is_loading = True
            self.progress = 0

    def get_value(self):
        multiplier = 2 ** (autoclickers[self.button_color].level // 10)
        return self.value * multiplier


class AutoClicker:
    def __init__(self, color, cost, rate):
        self.color = color
        self.cost = cost
        self.rate = rate
        self.level = 0

    def buy(self):
        global money
        if money >= self.cost:
            money -= self.cost
            self.level += 1
            self.cost = int(self.cost * 1.15)

    def update(self, button):
        if self.level > 0:
            button.progress += self.rate * self.level
            if button.progress >= button.max_progress:
                global money
                money += button.get_value()
                button.progress = 0


buttons = [
    Button(GREEN, (30, 50), 1, "green"),
    Button(BLUE, (30, 100), 2, "blue"),
    Button(ORANGE, (30, 150), 3, "orange"),
    Button(RED, (30, 200), 4, "red"),
    Button(PURPLE, (30, 250), 5, "purple"),
]

autoclickers = {
    "green": AutoClicker("green", cost=50, rate=1),
    "blue": AutoClicker("blue", cost=100, rate=2),
    "orange": AutoClicker("orange", cost=200, rate=3),
    "red": AutoClicker("red", cost=400, rate=4),
    "purple": AutoClicker("purple", cost=800, rate=5),
}


def draw_money():
    money_text = font.render(f"Money: ${money}", True, WHITE)
    screen.blit(money_text, (10, screen_height - 50))


def draw_save():
    save_text = font.render(f"Save", True, WHITE)
    screen.blit(save_text, (screen_width - 65, screen_height - 50))


def draw_shop():
    x = 10
    y = screen_height - 300
    button_height = 30
    button_width = 200

    for color, autoclicker in autoclickers.items():
        if money >= autoclicker.cost:
            button_color = GREEN
        else:
            button_color = RED

        button_rect = pygame.Rect(x, y, button_width, button_height)
        pygame.draw.rect(screen, button_color, button_rect, 2)

        shop_text = font.render(
            f"{color.capitalize()} Autoclick: ${autoclicker.cost}",
            True,
            WHITE,
        )
        text_rect = shop_text.get_rect(center=button_rect.center)
        screen.blit(shop_text, text_rect)

        y += 40


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
                            money, autoclickers = load_game(autoclickers)
                            menu_active = False
                        if i == 2:
                            running = False

    else:
        timer.tick(frame_rate)
        screen.fill(BLACK)

        for button in buttons:
            button.draw(screen)
            button.draw_level(screen, font)
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
        save_button_rect = pygame.Rect(screen_width - 65, screen_height - 50, 60, 30)
        if save_button_rect.collidepoint(mouse_pos):
            save_game(money, autoclickers)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                for button in buttons:
                    if button.clicked(mouse_pos):
                        button.start_loading()

                y = screen_height - 300
                for color, autoclicker in autoclickers.items():
                    shop_item_rect = pygame.Rect(10, y, 200, 30)
                    if shop_item_rect.collidepoint(mouse_pos):
                        autoclicker.buy()
                    y += 40

        pygame.display.flip()

pygame.quit()
