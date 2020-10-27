import unittest

from src.Dice import RegularDice, CrookedDice


class TestDice(unittest.TestCase):

    def setUp(self):
        self.regular_dice = RegularDice()
        self.crooked_dice = CrookedDice()

    def test__regular_dice_roll__check_dice_value_between_1_to_6(self):
        for _ in range(10):
            dice_value = self.regular_dice.roll()
            self.assertTrue(1 <= dice_value <= 6)

    def test__crooked_dice_roll__check_even_values(self):
        for _ in range(10):
            dice_value = self.crooked_dice.roll()
            self.assertTrue(dice_value % 2 == 0)


if __name__ == "__main__":
    unittest.main()
