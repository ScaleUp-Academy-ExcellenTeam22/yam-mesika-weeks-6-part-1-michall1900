def words_length(sentence: str) -> list[int]:
    """
    Receives string, calculates each word length, and returns words' length in a list.
    Note: Word is consecutive of characters that are without white spaces
    :param sentence: String.
    :return: List of words' length while their order is like their order in the sentence.
    """
    return [len(word) for word in sentence.split()]


def main_hi_hello() -> None:
    """
    Print words' length of some sentences.
    :return: None.
    """
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))


if __name__ == "__main__":
    main_hi_hello()
