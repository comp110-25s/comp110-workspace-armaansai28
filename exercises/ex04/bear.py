__author__ = "730560520"

"""File to define Bear class."""


class Bear:

    def __init__(self):
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        self.hunger_score += num_fish
