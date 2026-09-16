def isogram(string: str) -> bool:
    clean_string = string.lower()
    seen_letters = []

    for char in clean_string:
        if char.isalpha():
            if char in seen_letters:
                return False
            seen_letters.append(char)

    return True


if __name__ == "__main__":
    print(isogram("lumberjack"))
    print(isogram("alphabet"))
    print(isogram("six-year-old"))
    print(isogram("Subdermatoglyphic"))