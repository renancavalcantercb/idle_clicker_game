import config


class AutoClicker:
    def __init__(self, color, cost, rate):
        self.color = color
        self.cost = cost
        self.rate = rate
        self.level = 0

    def buy(self):
        if config.game_money >= self.cost:
            config.game_money -= self.cost
            self.level += 1
            self.cost = int(self.cost * 1.15)

    def update(self, button):
        if self.level > 0:
            button.progress += self.rate * self.level
            if not button.is_loading:
                button.start_loading()
            if button.progress >= button.max_progress:
                config.game_money += button.get_value()
                button.progress = 0
                button.is_loading = False


autoclickers = {
    "green": AutoClicker("green", cost=50, rate=1),
    "blue": AutoClicker("blue", cost=100, rate=2),
    "orange": AutoClicker("orange", cost=200, rate=3),
    "red": AutoClicker("red", cost=400, rate=4),
    "purple": AutoClicker("purple", cost=800, rate=5),
}
