__author__ = "730560520"

"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checks the age and keeps only the fish that are 3 or younger"""
        remaining_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                remaining_fish.append(fish)
        self.fish = remaining_fish

        """Checks the age and keeps only the bears that are 5 or younger"""
        remaining_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                remaining_bears.append(bear)
        self.bears = remaining_bears

    def remove_fish(self, amount: int) -> None:
        x = 0
        while x < amount and len(self.fish) > 0:
            self.fish.pop(0)
            x += 1

    def bears_eating(self) -> None:
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        remaining_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                remaining_bears.append(bear)
        self.bears = remaining_bears

    def repopulate_fish(self) -> None:
        original_fish = len(self.fish)
        baby_fish = (original_fish // 2) * 4
        x = 0
        while x < baby_fish:
            self.fish.append(Fish())
            x += 1

    def repopulate_bears(self) -> None:
        original_bears = len(self.bears)
        baby_bears = original_bears // 2
        x = 0
        while x < baby_bears:
            self.bears.append(Bear())
            x += 1

    def view_river(self) -> None:
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self) -> None:
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
