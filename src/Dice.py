import random
from abc import ABC, abstractmethod


class Dice(ABC):
    @abstractmethod
    def roll(self):
        pass


class RegularDice(Dice):
    """
    :return: random integer value between 1 to 6(both inclusive)
    """

    def roll(self):
        return random.randint(1, 6)


class CrookedDice(Dice):
    """
    :return: only even integer value between 2 to 7
    """

    def roll(self):
        return random.randrange(2, 7, 2)
