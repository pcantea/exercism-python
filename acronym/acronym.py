import re

def abbreviate(words):
    return ''.join(word[0] for word in re.sub(r'[^a-zA-Z\']', " ", words).upper().split())