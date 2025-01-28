"""Write a program to help plan a cozy tea party"""

__author__: str = "730560520"


def main_planner(guests: int) -> None:
    """Entrypoint for the program that displays details for the teaparty"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Computes the number of tea bags needed based on the number of people"""
    return people * 2


def treats(people: int) -> int:
    """Computes the # of treats needed based on the # of teas guests are
    expected to drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of the tea bags and the treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
