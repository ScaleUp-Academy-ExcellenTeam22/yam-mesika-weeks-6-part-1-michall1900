from functools import partial
from itertools import product


def full_names(first_names: list[str], last_names: list[str], min_length: int = 0) -> list[str]:
    """
    Returns list of all combinations of full names that could be combined from first names and
    last names lists that their length is bigger than the minimum wanted length.
    :param first_names: List of first names.
    :param last_names: List of last names.
    :param min_length: The minimum length of full name, by default = 0.
    :return: All of the combinations to full names that are bigger than minimum length.
    """
    return [" ".join(full_name).title() for full_name in list(product(first_names, last_names))
            if sum(len(name) for name in full_name) + 1 >= min_length]


def main_full_names() -> None:
    """
    Print all of the combinations to full names from first name list and last name list
    that are bigger than minimum length.
    :return:
    """
    full_names_with_specific_name = partial(full_names, ['avi', 'moshe', 'yaakov'], ['cohen', 'levi', 'mizrahi'])
    print(full_names_with_specific_name())
    print(full_names_with_specific_name(10))


if __name__ == "__main__":
    main_full_names()


