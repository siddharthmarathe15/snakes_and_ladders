import random
from abc import ABC, abstractmethod


class Dice(ABC):
    @abstractmethod
    def roll(self):
        pass


class RegularDice(Dice):
    def roll(self):
        return random.randint(1, 6)


class CrookedDice(Dice):
    def roll(self):
        return random.randrange(2, 7, 2)
