import unittest

from src.Dice import RegularDice
from src.Player import Player
from src.utilities import disable_print_statements_on_console


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.dice = RegularDice()
        self.player = Player("Test Player", self.dice)

    @disable_print_statements_on_console
    def test__chance_to_roll_dice__return_value_between_1_to_6(self):
        dice_value = self.player.chance_to_roll_dice()
        self.assertTrue(1 <= dice_value <= 6)

    @disable_print_statements_on_console
    def test__chance_to_roll_dice__return_int_value(self):
        dice_value = self.player.chance_to_roll_dice()
        self.assertIsInstance(dice_value, int)


if __name__ == "__main__":
    unittest.main()
