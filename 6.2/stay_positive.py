def get_positive_numbers() -> list[int]:
    """
    Get from the user list of numbers and return a list of the positive once after changing them into integers.
    :return: List's object of the positive numbers that the user inserted after changing them into integers.
    """
    return list(map(int, list(filter(lambda number: number >= 0, get_input_from_user()))))


def get_input_from_user() -> list[float]:
    """
    Getting from user list of numbers separated with ',' and return its input as a list after
    cast any number into float.
    Note: I assume that the input is valid.
    :return: List of numbers.
    """
    return list(map(float, input("Please enter list of numbers (separated with ','): ").split(",")))


def main_stay_positive() -> None:
    print("Your positive numbers after change them into integers are: ", get_positive_numbers())


if __name__ == "__main__":
    main_stay_positive()
