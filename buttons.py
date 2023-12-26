import pygame
from config import WHITE, GREEN, BLUE, RED, ORANGE, PURPLE
import config
from autoclickers import autoclickers


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
            config.game_money += self.get_value()
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


buttons = [
    Button(GREEN, (30, 50), 1, "green"),
    Button(BLUE, (30, 100), 2, "blue"),
    Button(ORANGE, (30, 150), 3, "orange"),
    Button(RED, (30, 200), 4, "red"),
    Button(PURPLE, (30, 250), 5, "purple"),
]
