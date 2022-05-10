def count_words(text: str) -> dict[str, int]:
    """
    Receives text, returns a dictionary with words from it as keys and the length of the word as a value.
    :param text: String.
    :return: A dictionary hows its keys are words (from text), and its values are their length.
    """
    text_with_just_letters = "".join(letter for letter in text if letter.isalnum() or letter.isspace())
    return {word.lower(): len(word) for word in text_with_just_letters.split()}


def main_count_words() -> None:
    """
    Take text and print the words in it and their length.
    :return: None.
    """
    text = """
        You see, wire telegraph is a kind of a very, very long cat.
        You pull his tail in New York and his head is meowing in Los Angeles.
        Do you understand this?
        And radio operates exactly the same way: you send signals here, they receive them there.
        The only difference is that there is no cat.
        """
    print(count_words(text))


if __name__ == "__main__":
    main_count_words()
