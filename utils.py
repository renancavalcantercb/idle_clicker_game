import json


def save_game(money, autoclickers):
    game_data = {
        "money": money,
        "autoclickers": {
            color: {"cost": autoclicker.cost, "level": autoclicker.level}
            for color, autoclicker in autoclickers.items()
        },
    }

    with open("savegame.json", "w") as file:
        json.dump(game_data, file)


def load_game(autoclickers):
    global money
    try:
        with open("savegame.json", "r") as file:
            game_data = json.load(file)
            money = game_data["money"]
            for color, data in game_data["autoclickers"].items():
                autoclickers[color].cost = data["cost"]
                autoclickers[color].level = data["level"]
    except FileNotFoundError:
        print("Save file not found. Starting a new game.")
    except json.JSONDecodeError:
        print("Error decoding the save file. Possible corrupted file.")

    return money, autoclickers
