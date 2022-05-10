from collections.abc import Callable
from typing import Generator, Iterable, Iterator, Union


def my_filter(function: Union[Callable, None], iterable: Iterable) -> Iterator[Generator]:
    """An implementation to filter function.

    Receive a boolean function and an iterable.
    Return all the iterable's values that the received function returns true while running on them.
    If None is received instead of a function, the function returns all values at the iterable that weighed true.
    :param function: A function that its return value equivalent to true/ false.
    :param iterable: Any iterable.
    :return: All the values that its return value is equivalent to true.
    """
    return (item for item in iterable if (function and function(item)) or (not function and item))


def main_my_filter() -> None:
    """Use my filter implementation to print some of its results.

    :return: None.
    """
    print(list(my_filter(lambda x: x >= 18, [0, 1, 4, 10, 20, 35, 56, 84, 120])))
    print(list(my_filter(None, [0, "", None, 0.0, True, False, "Hello"])))
    print(list(my_filter(lambda n: n > 0, [-2, -1, 0, 1, 2])))
    print(list(my_filter(sum, [(1, -1), (2, 5), (5, -3, -2), (1, 2, 3)])))


if __name__ == "__main__":
    main_my_filter()
