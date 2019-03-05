def is_pangram(sentence):
    sentence = sentence.lower()

    sentence = set(sentence)

    alphabet = [ch for ch in sentence if ord(ch) in range(ord('a'), ord('z')+1)]

    if len(alphabet) == 26:
        return True
    else:
        return False