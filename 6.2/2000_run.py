from collections.abc import Callable
from time import time


def timer(function: Callable, *args, **kwargs) -> float:
    """Receive a function and arguments for it and compute the time that took for it to run.

    :param function: Any function to check its running time.
    :param args: Function arguments.
    :param kwargs: Function arguments.
    :return: Function's running time.
    """
    start_time = time()
    function(*args, **kwargs)
    end_time = time()
    return end_time - start_time


def main_2000_run() -> None:
    """Use the timer function to check the running time of some functions.

    :return: None.
    """
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))


if __name__ == "__main__":
    main_2000_run()
