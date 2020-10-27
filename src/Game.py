from src.Board import Board
from src.Dice import RegularDice
from src.GameException import GameException
from src.Player import Player


class SnakesAndLadders:
    def __init__(self, player, board, turns):
        self.player = player
        self.board = board
        self.turns = turns

    def play(self):
        """
        The method describes the flow of the game. The game will be terminated either
        when the player reached maximum number of chances or the player has won the game
        """
        for _ in range(self.turns):
            try:
                initial_position = self.player.position
                dice_value = self.player.chance_to_roll_dice()
                self.board.move(self.player, dice_value)
                print(f"Player: {self.player.name} has moved from position: {initial_position} to position: {self.player.position}")
            except GameException as game_exception:
                print(game_exception.message)
                return
        print(f"\n\nGame over. You have reached maximum number of chances.")


snakes = {
    14: 7,
}

if __name__ == "__main__":
    dice = RegularDice()
    board = Board(snakes)
    player = Player("Sid", dice)
    game = SnakesAndLadders(player, board, 10)
    game.play()
