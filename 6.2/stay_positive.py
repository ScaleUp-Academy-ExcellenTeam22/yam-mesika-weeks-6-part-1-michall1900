def get_positive_numbers(numbers: list[float]) -> list[int]:
    """Get a list of numbers and return a list of the positive ones after changing them into integers.

    :param numbers: List of numbers.
    :return: List's object of the positive numbers that the user inserted after changing them into integers.
    """
    return [int(number) for number in numbers if number >= 0]


def get_input_from_user() -> list[float]:
    """Get from the user list of numbers separated with ',' and return its input as a list after
    casting them to float.
    Note: I assume that the input is valid.

    :return: List of numbers.
    """
    return [float(number) for number in input("Please enter list of numbers (separated with ','): ").split(",")]


def main_stay_positive() -> None:
    print("Your positive numbers after change them into integers are: ", get_positive_numbers(get_input_from_user()))


if __name__ == "__main__":
    main_stay_positive()
