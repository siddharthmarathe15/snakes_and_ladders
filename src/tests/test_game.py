import unittest
from unittest.mock import MagicMock

from src.Board import Board
from src.Dice import RegularDice
from src.Game import SnakesAndLadders
from src.Player import Player
from src.utilities import disable_print_statements_on_console


class TestGame(unittest.TestCase):

    def setUp(self):
        self.snakes = {14: 7}
        self.board = Board(self.snakes)
        self.dice = RegularDice()
        self.player = Player("Test Player", self.dice)
        self.game = SnakesAndLadders(self.player, self.board, 1)

    @disable_print_statements_on_console
    def test__play__check_for_single_chance(self):
        self.player.chance_to_roll_dice = MagicMock(return_value=2)
        self.game.play()
        self.assertEqual(self.player.position, 3)


if __name__ == "__main__":
    unittest.main()
