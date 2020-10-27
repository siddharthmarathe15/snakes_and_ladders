import unittest

from src.Board import Board
from src.Dice import RegularDice
from src.GameException import GameException
from src.Player import Player


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.dice = RegularDice()
        self.player = Player("Test Player", self.dice)
        self.snakes = {14: 7}
        self.board = Board(self.snakes)

    def test__move__check_player_position(self):
        starting_position = self.player.position
        dice_value = self.player.chance_to_roll_dice()
        self.board.move(self.player, dice_value)
        self.assertNotEqual(self.player.position, starting_position)

    def test__move__check_for_snake_bite(self):
        self.player.position = 10
        dice_value = 4
        self.board.move(self.player, dice_value)
        self.assertEqual(self.player.position, 7)

    def test__move__check_winning_condition(self):
        self.player.position = 99
        dice_value = 1
        with self.assertRaises(GameException) as ge:
            self.board.move(self.player, dice_value)
        self.assertEqual(ge.exception.message, "\n\nCongratulations! Test Player won the game")


if __name__ == "__main__":
    unittest.main()
