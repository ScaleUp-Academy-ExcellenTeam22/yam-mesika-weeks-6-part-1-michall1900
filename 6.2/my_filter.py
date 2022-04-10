from collections.abc import Callable
from typing import Generator, Iterable, Iterator, Union


def my_filter(function: Union[Callable, None], iterable: Iterable) -> Iterator[Generator]:
    """
    Implement filter function - receives function and iterable and return all of the
    values that the function return for the value that weighed true.
    If None is received instead of a function, the function returns all values at the iterable that weighed true.
    :param function: Any function that its return value could be weighed to true/ false. Could be None instead.
    :param iterable: Any iterable.
    :return: All of the values that its return value is weighed to true.
    """
    return (item for item in iterable if (function and function(item)) or (not function and item))


def main_my_filter() -> None:
    """
    Use my filter implementation to print some of its results.
    :return: None.
    """
    print(list(my_filter(lambda x: x >= 18, [0, 1, 4, 10, 20, 35, 56, 84, 120])))
    print(list(my_filter(None, [0, "", None, 0.0, True, False, "Hello"])))
    print(list(my_filter(lambda n: n > 0, [-2, -1, 0, 1, 2])))
    print(list(my_filter(sum, [(1, -1), (2, 5), (5, -3, -2), (1, 2, 3)])))


if __name__ == "__main__":
    main_my_filter()
