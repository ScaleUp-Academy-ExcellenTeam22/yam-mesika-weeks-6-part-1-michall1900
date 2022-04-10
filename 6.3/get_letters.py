def get_letters() -> list[str]:
    """
    Return all of the ABC letters (upper and lower) inside a list.
    :return: A list including all of the ABC letters (upper and lower).
    """
    return [chr(ascii_number) for ascii_number in range(ord("A"), ord("z")+1)
            if ascii_number not in range(ord("Z")+1, ord("a"))]


def main_get_letters() -> None:
    """
    Print all of the ABC letters.
    :return: None.
    """
    print(get_letters())


if __name__ == "__main__":
    main_get_letters()
