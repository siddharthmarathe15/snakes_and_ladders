import time


class Player:
    def __init__(self, name, dice):
        self.name = name
        self.position = 1
        self.dice = dice

    def chance_to_roll_dice(self):
        print(f"\nRolling dice for player: {self.name}")
        time.sleep(2)
        dice_value = self.dice.roll()
        print(f"It's [{dice_value}]")
        return dice_value

    def get_player_position(self):
        return self.position

    def get_player_name(self):
        return self.name
