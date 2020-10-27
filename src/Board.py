import time

from src.GameException import GameException


class Board:
    def __init__(self, snakes):
        self.starting_position = 1
        self.end_position = 100
        self.snakes = snakes

    def move(self, player, dice_value):
        """
        The method updates the position of the player according to the dice value and also checks for the winning case.
        """
        updated_position = player.position + dice_value

        if updated_position > self.end_position:
            print("You need " + str(self.end_position - player.position) + "to win the game. Keep rolling.")

        if updated_position in self.snakes.keys():
            print(f"Player: {player.name} got a snake bite. Rolled down from {player.position} to "
                  f"{self.snakes.get(updated_position)}")
            time.sleep(2)
            player.position = self.snakes.get(updated_position)
        else:
            player.position = updated_position

        self.check_for_winner(player)

    def check_for_winner(self, player):
        """
        The method checks for the winning case. If the player reaches the end point then the game is over.
        """
        if player.position == self.end_position:
            raise GameException(f"\n\nCongratulations! {player.name} won the game")
