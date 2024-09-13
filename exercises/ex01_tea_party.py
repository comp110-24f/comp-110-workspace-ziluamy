"""tea party exercise"""

__author__ = "730621701"


def main_planner(guests: int) -> None:
    """bring all of these functions together in a “main planner” function that calls each and produces printed output."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # here we need to call the tea_bags and treats function


def tea_bags(people: int) -> int:
    """compute the number of tea bags needed based on number of guests"""
    return people * 2


def treats(people: int) -> int:
    """compute the number of treats needed based on the number of teas guests are expecting to drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """compute the cost of the tea bags and the treats combined"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
