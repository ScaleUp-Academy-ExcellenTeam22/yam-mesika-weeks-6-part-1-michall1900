from collections.abc import Callable
from time import time


def timer(function: Callable, *args, **kwargs) -> float:
    """
    Receives function and arguments for her and return the time that took for her to run.
    :param function: Any function to check her running time.
    :param args: Arguments for function.
    :param kwargs: Arguments for function.
    :return: Function running time.
    """
    start_time = time()
    function(*args, **kwargs)
    end_time = time()
    return end_time - start_time


def main_2000_run() -> None:
    """
    Using timer function to check what is the running time for some functions.
    :return: None.
    """
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))


if __name__ == "__main__":
    main_2000_run()
