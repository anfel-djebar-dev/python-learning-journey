import string

def is_pangram(sentence: str) -> bool:
    clean_sentence = sentence.lower()
    
    for letter in string.ascii_lowercase:
        if letter not in clean_sentence:
            return False
            
    return True


if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog"))
    print(is_pangram("The quick brown fox jumps over the dog"))